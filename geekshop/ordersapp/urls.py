from django.urls import path
import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.OrderLists.as_view(), name='orders'),
    path('craete/', ordersapp.OrderCreateLists.as_view(), name='orders_create'),


]