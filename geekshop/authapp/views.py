from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse

from basketapp.models import Basket


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
                messages.error(request, 'Ваш акаунт не активен!!!')
                return render(request, 'authapp/login.html')
        else:
            messages.error(request, 'Неверные данные для входа в систему.')
            return render(request, 'authapp/login.html')

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
            form.save()
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
