from django.shortcuts import render, HttpResponseRedirect
from authapp.models import User
from mainapp.models import ProductCategory
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryAdminRegisterForm, \
    CategoryAdminUpdateForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView


# Create your views here.
@user_passes_test(lambda user: user.is_superuser)
def index(request):
    return render(request, 'adminapp/index.html')


class UserListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda user: user.is_superuser)
# def admin_users(request):
#     context = {
#         'users': User.objects.all()
#     }
#     return render(request, 'adminapp/admin-users-read.html', context)

class UserCreateView(CreateView):
    model = User
    form_class = UserAdminRegisterForm
    template_name = 'adminapp/admin-users-create.html'
    success_url = reverse_lazy('admin_staff:admin_users')

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda user: user.is_superuser)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin_staff:admin_users'))
#         else:
#             return HttpResponseRedirect(reverse('admin_staff:admin_users'))
#     form = UserAdminRegisterForm()
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'adminapp/admin-users-create.html', context)

class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    form_class = UserAdminProfileForm

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        # context['title'] = 'Geekshop - Редактирование пользователя'
        context.update({'title': 'Geekshop - Редактирование пользователя'})

        return context

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda user: user.is_superuser)
# def admin_users_update(request, user_pk=None):
#     user = User.objects.get(pk=user_pk)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin_staff:admin_users'))
#         # else:
#         #     return render(request, 'adminapp/admin-users-read.html')
#     else:
#         form = UserAdminProfileForm(instance=user)
#
#     context = {
#         'form': form,
#         'user': user,
#     }
#     return render(request, 'adminapp/admin-users-update-delete.html', context)

class UserRemoveView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserRemoveView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda user: user.is_superuser)
# def admin_users_remove(request, user_id=None):
#     user = User.objects.get(id=user_id)
#     # user.delete() # not good!
#     user.is_active = False
#     user.save()
#
#     return HttpResponseRedirect(reverse('admin_staff:admin_users'))


# ==============================categories=============================================================== #
class CategoryListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/admin-category-read.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser))
def dispatch(self, request, *args, **kwargs):
    return super(CategoryListView, self).dispatch(request, *args, **kwargs)


# def admin_category(request):
#     categories = ProductCategory.objects.all()
#     context = {
#         'categories': categories,
#     }
#     return render(request, 'adminapp/admin-category-read.html', context)
class CategoryCreateView(CreateView):
    model = ProductCategory
    form_class = CategoryAdminRegisterForm
    template_name = 'adminapp/admin-category-create.html'
    success_url = reverse_lazy('admin_staff:admin_category')

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryCreateView, self).dispatch(request, *args, **kwargs)


# def admin_category_create(request):
#     if request.method == 'POST':
#         form = CategoryAdminRegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin_staff:admin_category'))
#         else:
#             messages.error('Что-то не так!!!')
#             return HttpResponseRedirect(reverse('admin_staff:admin_category'))
#     form = CategoryAdminRegisterForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'adminapp/admin-category-create.html', context)


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/admin-category-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_category')
    form_class = CategoryAdminUpdateForm

    # def get_context_data(self, **kwargs):
    #     context = super(CategoryUpdateView, self).get_context_data(**kwargs)
    #     context.update({'title': 'Geekshop - Редактирование категории'})
    #
    #     return context
    #
    # @method_decorator(user_passes_test(lambda user: user.is_superuser))
    # def dispatch(self, request, *args, **kwargs):
    #     return super(CategoryUpdateView, self).dispatch(request, *args, **kwargs)


# def admin_category_update(request, categ_id):
#     category = ProductCategory.objects.get(id=categ_id)
#     if request.method == 'POST':
#         form = CategoryAdminUpdateForm(request.POST or None, instance=category)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin_staff:admin_category'))
#         else:
#             return HttpResponseRedirect(reverse('admin_staff:admin_category'))
#     form = CategoryAdminUpdateForm()
#     context = {
#         'form': form,
#         'category': category,
#     }
#     return render(request, 'adminapp/admin-category-update-delete.html', context)

class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/admin-category-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_category')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryDeleteView, self).dispatch(request, *args, **kwargs)

# def admin_category_delete(request, categ_id):
#     print(f'--------------------------------------------------{categ_id}')
#     category = ProductCategory.objects.get(id=categ_id)
#     print(f'-------------------------------------------------->{category}')
#     category.is_active = False
#     category.save()
#
#     return HttpResponseRedirect(reverse('admin_staff:admin_category'))
