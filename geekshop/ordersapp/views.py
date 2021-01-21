from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render

# покажем пользователю его заказы
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from basketapp.models import Basket
from ordersapp.forms import OrderItemForm
from ordersapp.models import Order, OrderItems


class OrderLists(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderCreateLists(CreateView):
    model = Order
    fields = []  # поля не понадобятся
    success_url = reverse_lazy('orders_users:orders')

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        """Предобработка"""
        data = super(OrderCreateLists, self).get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order, OrderItems, form=OrderItemForm, extra=1)

        if self.request.POST:
            formset = OrderFormSet(self.request.POST)  # весьPOST запрос передаем
            print(f'========>>>>{formset}')
        else:
            basket_items = Basket.objects.filter(user=self.request.user)
            if basket_items.exists():
                OrderFormSet = inlineformset_factory(Order, OrderItems, form=OrderItemForm, extra=basket_items.count())
                formset = OrderFormSet()  # пустой запрос передаем
                for num, form in enumerate(formset.forms):
                    form.initial['product'] = basket_items[num].product
                    form.initial['quantity'] = basket_items[num].quantity
                # basket_items.delete()
            else:
                formset = OrderFormSet()  # пустой запрос передаем
        data['orderitems'] = formset
        print(f'======++++++====>>>>{data}')

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

            # удаляем пустой заказ
        if self.object.get_total_summ() == 0:
            self.object.delete()
        # return super(OrderItemsCreate, self).form_valid(form)
        return super(OrderCreateLists, self).form_valid(form)
