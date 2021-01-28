from django.urls import path
import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.OrderLists.as_view(), name='orders'),
    path('craete/', ordersapp.OrderCreateLists.as_view(), name='orders_create'),
    path('update/<pk>/', ordersapp.OrderUpdateLists.as_view(), name='orders_update'),
    path('delete/<pk>/', ordersapp.OrderDeleteLists.as_view(), name='orders_delete'),
    path('detail/<pk>/', ordersapp.OrderReadLists.as_view(), name='orders_read'),
    path('forming/<pk>/', ordersapp.order_forming_complete, name='order_forming_complete'),

    path('product/<pk>/price/', ordersapp.get_product_price, name='get_product_price'),

]
