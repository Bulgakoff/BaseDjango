from django.db import models

# Create your models here.
from basketapp.models import Basket
from geekshop import settings
from mainapp.models import Products


class Order(models.Model):
    FORMING = 'FM'
    SEND_TO_PROCEED = 'STP'
    PROCEED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    DONE = 'DN'
    CANSEL = 'CNC'

    ORDER_STATUSES = (
        (FORMING, 'формируется'),
        (SEND_TO_PROCEED, 'отправлен на обработку'),
        (PROCEED, 'обработан'),
        (PAID, 'оплачен'),
        (READY, 'готов к выдаче'),
        (DONE, 'выдан '),
        (CANSEL, 'отменен'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # AUTH_USER_MODEL - владелец
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменен')

    status = models.CharField(max_length=3,
                              default=FORMING,
                              verbose_name='Статус',
                              choices=ORDER_STATUSES)

    is_active = models.BooleanField(default=True, verbose_name='Активен')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created_at',)

    def __str__(self):
        return 'Текущий заказ: {}'.format(self.id)

    def get_total_quantity(self):
        # baskets = Basket.objects.filter(user=self.user)
        # baskets = self.orderitems.select_related()
        baskets = OrderItems.order.select_related()
        return sum(basket.quantity for basket in baskets)

    def get_total_summ(self):
        # baskets = Basket.objects.filter(user=self.user)
        print(f'++++baskets[]+++>>>>{self.orderitems.select_related()}')
        baskets = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity * x.product.price, baskets)))
        # return sum(basket.get_ordered_products_cost() for basket in baskets)

    def get_summary(self):
        items = self.orderitems.select_related()
        # orderitems <== order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
        return {
            'total_cost': sum(list(map(lambda x: x.quantity * x.product.price, items))),
            'total_quantity': sum(list(map(lambda x: x.quantity, items))),
        }

    # переопределяем метод, удаляющий объект
    def delete(self):
        for item in self.orderitems.select_related():
            print(f'--item====item>>>>{self.orderitems.select_related()}')
            item.product.guantity += item.quantity
            item.product.save()

        self.is_active = False
        self.save()


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='количество')

    def get_ordered_products_cost(self):
        return self.quantity * self.product.price

    @staticmethod
    def get_item(pk):
        return OrderItems.objects.filter(pk=pk).first()
