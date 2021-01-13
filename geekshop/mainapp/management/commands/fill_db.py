from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Products
# from django.contrib.auth.models import User
from authapp.models import User


import json
import os

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categs')

        ProductCategory.objects.all().delete()
        # [ProductCategory.objects.create(**category) for category in categories]
        for category in categories:
            ProductCategory.objects.create(**category)
            # new_category = ProductCategory(**category)
            # new_category.save()

        products = load_from_json('prods')

        Products.objects.all().delete()
        for product in products:
            category_name = product["category"]
            # Получаем категорию по имени
            _category = ProductCategory.objects.get(name=category_name)
            # _category = ProductCategory.objects.filter(name=category_name).first()
            # QuerySet[] берем первый
            # Заменяем название категории объектом
            product['category'] = _category
            Products.objects.create(**product)
            # new_product = Product(**product)
            # new_Products.save()

        # # Создаем суперпользователя при помощи менеджера модели
        # if not User.objects.filter(username='django').exists():
        #     User.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains')
        if not User.objects.filter(username='django').exists():
            User.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains',age=25)
