from django.db import transaction
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

# покажем пользователю его заказы
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from basketapp.models import Basket
from mainapp.models import Products
from ordersapp.forms import OrderItemForm
from ordersapp.models import Order, OrderItems


class OrderLists(ListView):
    model = Order

    def get_queryset(self):
        """Отдаст все 'чеки' определенного пользователя"""
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
            formset = OrderFormSet(self.request.POST, instance=self.object)  # весьPOST запрос передаем
            print(f'===formset===>>>>{formset}')
        else:
            basket_items = Basket.objects.filter(user=self.request.user)

            if basket_items.exists():
                OrderFormSet = inlineformset_factory(Order, OrderItems, form=OrderItemForm, extra=basket_items.count())
                formset = OrderFormSet(instance=self.object)  # пустой запрос передаем
                for num, form in enumerate(formset.forms):
                    form.initial['product'] = basket_items[num].product
                    form.initial['quantity'] = basket_items[num].quantity
                    form.initial['price'] = basket_items[num].product.price
                # basket_items.delete()
            else:
                formset = OrderFormSet(instance=self.object)  # пустой запрос передаем
        data['orderitems'] = formset
        print(f'====data+++====>>>>{data}')
        print(f'====data+++"orderitems"==после==>>>>{data["orderitems"]}')

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']
        print(f'====+++orderitems+++====>>>>{orderitems}')

        with transaction.atomic():
            Basket.objects.filter(user=self.request.user).delete()
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

    # ======================«OrderItemsUpdate»========================


class OrderUpdateLists(UpdateView):
    model = Order
    fields = []  # поля не понадобятся
    success_url = reverse_lazy('orders_users:orders')

    def get_context_data(self, **kwargs):
        """Предобработка"""
        data = super(OrderUpdateLists, self).get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order, OrderItems, form=OrderItemForm, extra=1)

        if self.request.POST:
            formset = OrderFormSet(self.request.POST, instance=self.object)

            print(f'===formset===>>>>{formset}')
            print(f'===self.object===>>>>{self.object}')
            print(f'===self.request.user.id===>>>>{self.request.user.id}')
        else:
            formset = OrderFormSet(instance=self.object)  # пустой запрос передаем
            for form in formset.forms:
                if form.instance.pk:
                    form.initial['price'] = form.instance.product.price
            data.update({'orderitems': formset})
            # data['orderitems'] = formset
            # data.update({'orderitems': formset})
            print(f'====data+++====>>>>{data}')

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']
        print(f'===orderitems+++====>>>>{orderitems}')

        with transaction.atomic():
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

            # удаляем пустой заказ
        if self.object.get_total_summ() == 0:
            self.object.delete()
        # return super(OrderItemsCreate, self).form_valid(form)
        return super(OrderUpdateLists, self).form_valid(form)

    # def basket_add(self, request, pk=None):
    #     product = get_object_or_404(Products, id=pk)
    #     baskets = Basket.objects.filter(user=request.user, product=product)
    #     if not baskets.exists():
    #         basket = Basket(user=request.user, product=product)
    #         basket.quantity += 1
    #         basket.save()
    #         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #     else:
    #         basket = baskets.first()
    #         basket.quantity += 1
    #         basket.save()
    #         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #
    #
    #

    # ================OrderDeleteLists=======================


class OrderDeleteLists(DeleteView):
    model = Order
    success_url = reverse_lazy('orders_users:orders')

    # ================OrderDetailLists=============================


class OrderReadLists(DetailView):
    model = Order

    # ================order_forming_complete=============================


def order_forming_complete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.SEND_TO_PROCEED
    order.save()

    return HttpResponseRedirect(reverse('orders_users:orders'))


# @receiver(pre_save, sender=Basket)
# @receiver(pre_save, sender=OrderItems)
# def product_quantity_update_save(sender, update_fields, instance, **kwargs):
#     if update_fields is 'quantity' or 'product':
#         if instance.pk:
#             # instance.product.guantity -= instance.quantity - sender.objects.filter(instance.pk).first().quantity
#             instance.product.guantity -= instance.quantity - sender.get_item(instance.pk).quantity
#         else:
#             instance.product.guantity -= instance.quantity
#         instance.product.save()


# @receiver(pre_delete, sender=Basket)
# @receiver(pre_delete, sender=OrderItems)
# def product_quantity_update_delete(sender, instance, **kwargs):
#     instance.product.guantity += instance.quantity
#     instance.product.save()
def get_product_price(request, pk):
    if request.is_ajax():
        product_item = Products.objects.filter(pk=int(pk)).first()
        if product_item:
            return JsonResponse({'price': product_item.price})
        return JsonResponse({'price': 0})


