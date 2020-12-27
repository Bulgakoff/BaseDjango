from django.shortcuts import render, HttpResponseRedirect
from authapp.models import User
from mainapp.models import ProductCategory
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryAdminRegisterForm
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView

# Create your views here.
@user_passes_test(lambda user: user.is_superuser)
def index(request):
    return render(request, 'adminapp/index.html')

class UserListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'

# @user_passes_test(lambda user: user.is_superuser)
# def admin_users(request):
#     context = {
#         'users': User.objects.all()
#     }
#     return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda user: user.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_category_create'))
        else:
            return HttpResponseRedirect(reverse('admin_staff:admin_category_create'))
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


def admin_category(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'adminapp/admin-category-read.html', context)


def admin_category_create(request):
    if request.method == 'POST':
        form = CategoryAdminRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_category'))
        else:
            return HttpResponseRedirect(reverse('admin_staff:admin_category'))
    form = CategoryAdminRegisterForm()
    contex = {
        'form': form,
    }

    return render(request, 'adminapp/admin-category-create.html', contex)


def admin_category_update(request, categ_id):
    category = ProductCategory.objects.get(id=categ_id)
    if request.method == 'POST':
        form = CategoryAdminRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_category'))
        else:
            return HttpResponseRedirect(reverse('admin_staff:admin_category'))
    form = CategoryAdminRegisterForm()
    contex = {
        'form': form,
        'category': category,
    }
    return render(request, 'adminapp/admin-category-update-delete.html', contex)

def admin_category_delete(request, categ_id):
    category = ProductCategory.objects.get(id=categ_id)
    category.delete()

    return render(request, 'adminapp/admin-category-update-delete.html')