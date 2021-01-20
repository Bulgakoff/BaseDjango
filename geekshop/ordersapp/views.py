from django.shortcuts import render

# покажем пользователю его заказы
from django.views.generic import ListView

from ordersapp.models import Order


class OrderLists(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


