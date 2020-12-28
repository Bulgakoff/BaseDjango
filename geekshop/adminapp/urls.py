from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('users/', adminapp.UserListView.as_view(), name='admin_users'),
    path('users/create/', adminapp.UserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>/', adminapp.UserUpdateView.as_view(), name='admin_users_update'),
    path('users/remove/<int:pk>/', adminapp.UserRemoveView.as_view(), name='admin_users_remove'),

    path('users/category/', adminapp.admin_category, name='admin_category'),
    path('users/category/create/', adminapp.admin_category_create, name='admin_category_create'),
    path('users/category/update/<int:categ_id>/', adminapp.admin_category_update, name='admin_category_update'),
    path('users/category/delete/<int:categ_id>/', adminapp.admin_category_delete, name='admin_category_delete'),
]
