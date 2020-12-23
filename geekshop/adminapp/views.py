from django.shortcuts import render, HttpResponseRedirect
from authapp.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
@user_passes_test(lambda user: user.is_superuser)
def index(request):
    return render(request, 'adminapp/index.html')

@user_passes_test(lambda user: user.is_superuser)
def admin_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', context)

@user_passes_test(lambda user: user.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
        else:
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    form = UserAdminRegisterForm()
    contex = {
        'form': form,
    }

    return render(request, 'adminapp/admin-users-create.html', contex)

@user_passes_test(lambda user: user.is_superuser)
def admin_users_update(request, user_pk=None):
    user = User.objects.get(pk=user_pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
        # else:
        #     return render(request, 'adminapp/admin-users-read.html')
    else:
        form = UserAdminProfileForm(instance=user)

    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'adminapp/admin-users-update-delete.html', context)

@user_passes_test(lambda user: user.is_superuser)
def admin_users_remove(request, user_id=None):
    user = User.objects.get(id=user_id)
    # user.delete() # not good!
    user.is_active = False
    user.save()

    return HttpResponseRedirect(reverse('admin_staff:admin_users'))
