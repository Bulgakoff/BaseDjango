from django.db import models
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

    def __str__(self):
        return f'Корзина для {self.user.username}|Продукт  для {self.product.name}'

    def summa_product(self):
        return self.quantity * self.product.price

    def total_qu(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.quantity for basket in baskets)

    def total_summa(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.summa_product() for basket in baskets)

    @staticmethod
    def get_product(user,product):
        return Basket.objects.filter(user=user,product=product).order_by('price')

    # def delete(self):
    #     self.product.guantity += self.quantity
    #     self.product.save()
    #     super(Basket, self).delete()
