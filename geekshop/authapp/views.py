from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm, ShopUserProfileEditForm
from django.contrib import auth, messages
from django.urls import reverse

from authapp.models import User
from basketapp.models import Basket


def send_verify_email(user):
    """Отправка почтового сообщения пользователю"""
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])
    print(f'++++++>{verify_link}')
    subject = f'Подтверждение учетной записи {user.username}'
    message = f'Для подтверждения учетной записи {user.username} на портале \
    {settings.DOMAIN} перейдите по ссылке: \n{settings.DOMAIN}{verify_link}'
    print(message)
    print(
        f'----send_mail()» получим число успешно отправленных сообщений--->>{send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)}')

    # message = f'Для Подтверждения прейдите по ссылке {settings.DOMAIN} {verify_link}'
    return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activ_key):
    """Активация пользователя
       Теперь необходимо реализовать механизм активации пользователя при переходе по ссылке
       из сообщения. URL адрес уже прописан в диспетчере.
     """
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activ_key and not user.is_activation_key_expired():
            user.is_active = True
            user.activation_key = None
            user.save()
            auth.login(request, user)
            return render(request, 'authapp/verification.html')
        else:
            print(f'error activation user: {user}')
            return render(request, 'authapp/verification.html')

    except Exception as ex:
        print(f'error activation user : {ex.args}')
        return HttpResponseRedirect(reverse('main'))


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user and user.is_active:
                auth.login(request, user)
                messages.error(request, 'Ваш акаунт активен!!!')
                return HttpResponseRedirect(reverse('main'))
            else:
                context = {'form': form}
                messages.error(request, 'Ваш акаунт не активен!!!')
                return render(request, 'authapp/login.html', context)
        else:
            context = {'form': form}
            messages.error(request, 'Неверные данные для входа в систему.')
            return render(request, 'authapp/login.html', context)

    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


# def get_basket(user):
#     if user.is_authenticated:
#         basket = Basket.objects.filter(user=user)
#         return  basket
#     else:
#         return []


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        profile_form= ShopUserProfileEditForm(data=request.POST, instance=request.user.shopuserprofile)
        if form.is_valid()  and profile_form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:profile'))
        else:
            messages.error(request, 'Введены данные не корректно')
            return render(request, 'authapp/login.html')
    else:
        form = UserProfileForm(instance=request.user)
        profile_form= ShopUserProfileEditForm(instance=request.user.shopuserprofile)

    # baskets = Basket.objects.filter(user=request.user)
    context = {
        'form': form,
        'profile_form': profile_form,
        # 'baskets': get_basket(request.user),
    }
    return render(request, 'authapp/profile.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if send_verify_email(user):
                print('сообщение подтверждения отправлено')
                messages.success(request, 'Регистрация прошла успешно')
                return HttpResponseRedirect(reverse('auth:login'))
            else:
                print('ошибка отправки сообщения')
                return HttpResponseRedirect(reverse('auth:login'))
        else:
            messages.error(request, 'Регистрация провалилась')
            return HttpResponseRedirect(reverse('auth:login'))
    form = UserRegisterForm()
    context = {
        'form': form,
    }

    return render(request, 'authapp/register.html', context)
