from django.shortcuts import render, HttpResponseRedirect
from authapp.models import User
from mainapp.models import ProductCategory
from mainapp.models import Products
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryAdminRegisterForm, \
    CategoryAdminUpdateForm, ProductAdminRegisterForm, ProductAdminUpdateForm
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

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    form_class = UserAdminRegisterForm
    template_name = 'adminapp/admin-users-create.html'
    success_url = reverse_lazy('admin_staff:admin_users')

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


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


# ==============================categories=============================================================== #
class CategoryListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/admin-category-read.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser))
def dispatch(self, request, *args, **kwargs):
    return super(CategoryListView, self).dispatch(request, *args, **kwargs)


class CategoryCreateView(CreateView):
    model = ProductCategory
    form_class = CategoryAdminRegisterForm
    template_name = 'adminapp/admin-category-create.html'
    success_url = reverse_lazy('admin_staff:admin_category')

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryCreateView, self).dispatch(request, *args, **kwargs)


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/admin-category-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_category')
    form_class = CategoryAdminUpdateForm


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

    # =========================products================================


class ProductsListView(ListView):
    model = Products
    template_name = 'adminapp/admin-products-read.html'


class ProductsCreateView(CreateView):
    model = Products
    form_class = ProductAdminRegisterForm
    template_name = 'adminapp/admin-products-create.html'
    success_url = reverse_lazy('admin_staff:admin_products')

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductsCreateView, self).dispatch(request, *args, **kwargs)


class ProductsUpdateView(UpdateView):
    model = Products
    template_name = 'adminapp/admin-products-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_products')
    form_class = ProductAdminUpdateForm

    def get_context_data(self, **kwargs):
        context = super(ProductsUpdateView, self).get_context_data(**kwargs)
        # context['title'] = 'Geekshop - Редактирование пользователя'
        context.update({'title': 'Geekshop - Редактирование продукта'})

        return context

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductsUpdateView, self).dispatch(request, *args, **kwargs)
