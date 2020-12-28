from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('users/', adminapp.UserListView.as_view(), name='admin_users'),
    path('users/create/', adminapp.UserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>/', adminapp.UserUpdateView.as_view(), name='admin_users_update'),
    path('users/remove/<int:pk>/', adminapp.UserRemoveView.as_view(), name='admin_users_remove'),

    path('users/category/', adminapp.CategoryListView.as_view(), name='admin_category'),
    path('users/category/create/', adminapp.CategoryCreateView.as_view(), name='admin_category_create'),
    path('users/category/update/<int:pk>/', adminapp.CategoryUpdateView.as_view(), name='admin_category_update'),
    path('users/category/delete/<int:pk>/', adminapp.CategoryDeleteView.as_view(), name='admin_category_delete'),

    path('users/products/', adminapp.ProductsListView.as_view(), name='admin_products'),
    # path('users/products/create/', adminapp.CategoryCreateView.as_view(), name='admin_category_create'),
    # path('users/products/update/<int:pk>/', adminapp.CategoryUpdateView.as_view(), name='admin_category_update'),
    # path('users/products/delete/<int:pk>/', adminapp.CategoryDeleteView.as_view(), name='admin_category_delete'),
]
