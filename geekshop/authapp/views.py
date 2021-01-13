from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse

from basketapp.models import Basket


def send_verify_email(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])
    subject = f'Подтверждение учетной записи {user.username}'
    message = f'Для подтверждения учетной записи {user.username} на портале \
    {settings.DOMAIN} перейдите по ссылке: \n{settings.DOMAIN}{verify_link}'

    # message = f'Для Подтверждения прейдите по ссылке {settings.DOMAIN} {verify_link}'
    return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activ_key):
    pass


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
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


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:profile'))
        else:
            messages.error(request, 'Введены данные не корректно')
            return render(request, 'authapp/login.html')
    else:
        form = UserProfileForm(instance=request.user)

    baskets = Basket.objects.filter(user=request.user)
    context = {
        'form': form,
        'baskets': baskets,
    }
    return render(request, 'authapp/profile.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if send_verify_email(user):
                print('сообщение подтверждения отправлено')
                return HttpResponseRedirect(reverse('auth:login'))
            else:
                print('ошибка отправки сообщения')
                return HttpResponseRedirect(reverse('auth:login'))
            messages.success(request, 'Регистрация прошла успешно')
            return HttpResponseRedirect(reverse('auth:login'))
        else:
            messages.error(request, 'Регистрация прошла провалилась')
            return HttpResponseRedirect(reverse('auth:login'))
    form = UserRegisterForm()
    contex = {
        'form': form,
    }

    return render(request, 'authapp/register.html', contex)
