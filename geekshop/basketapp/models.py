from django.db import models
from authapp.models import User
from mainapp.models import Products


class Basket(models.Model):
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
