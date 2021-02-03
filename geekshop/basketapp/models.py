from django.db import models
from django.utils.functional import cached_property

from authapp.models import User
from mainapp.models import Products


# class BasketQuerySet(models.QuerySet):
#     def delete(self):
#         for object in self:
#             object.product.guantity += object.quantity
#             object.product.save()
#         super(BasketQuerySet, self).delete()


class Basket(models.Model):
    # objects = BasketQuerySet.as_manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    @cached_property
    # @property
    def get_items_basket_cached(self):
        return Basket.objects.filter(user=self.user).select_related()
        # return self.user.basket_set.select_related()

    def __str__(self):
        return f'Корзина для {self.user.username}|Продукт  для {self.product.name}'

    def summa_product(self):
        return self.quantity * self.product.price

    def total_qu(self):
        # baskets = Basket.objects.filter(user=self.user)
        baskets = self.get_items_basket_cached  # если используется @cached_property  стр.23 кэшировани
        # е то обращение происходит не как к методу а как к свойству
        return sum(basket.quantity for basket in baskets)

    def total_summa(self):
        # baskets = Basket.objects.filter(user=self.user)
        baskets = self.get_items_basket_cached  # если используется @cached_property кэширование
        # то обращение происходит не как к методу а как к свойству
        return sum(basket.summa_product() for basket in baskets)

    # def delete(self):
    #     self.product.guantity += self.quantity
    #     self.product.save()
    #     super(Basket, self).delete()
