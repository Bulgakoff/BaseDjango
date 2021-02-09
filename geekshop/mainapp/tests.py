from django.core.management import call_command
from django.test import TestCase, Client

from mainapp.models import ProductCategory, Products


class TestMainappTestCase(TestCase):
    def setUp(self):
        category = ProductCategory.objects.create(
            name='Test1'
        )
        Products.objects.create(
            category=category,
            name='prod_test1'
        )
        Products.objects.create(
            category=category,
            name='prod_test2'
        )
        self.client = Client()


    def test_mainapp_pages(self):
        response = self.client.get('/')
        print(f'====================>{response}')
        self.assertEqual(response.status_code, 200)


    def test_mainapp_shop(self):
        response = self.client.get('/products/')
        print(f'====================>{response}')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/products/1/')
        print(f'====================>{response}')
        self.assertEqual(response.status_code, 200)

        for category in ProductCategory.objects.all():
            response = self.client.get(f'/products/{category.pk}/')
            print(f'====================>{response}')
            self.assertEqual(response.status_code, 200)

class ProductsTestCase(TestCase):
    def setUp(self):
        category = ProductCategory.objects.create(name="cat1")
        self.product_1 = Products.objects.create(name="prod1",
                                                 category=category,
                                                 price=1999.5,
                                                 guantity=150)

        self.product_2 = Products.objects.create(name="prod2",
                                                 category=category,
                                                 price=2998.1,
                                                 guantity=125,
                                                 is_active=False)

        self.product_3 = Products.objects.create(name="prod3",
                                                 category=category,
                                                 price=998.1,
                                                 guantity=115)

    def test_product_get(self):
        product_1 = Products.objects.get(name="prod1")
        product_2 = Products.objects.get(name="prod2")
        self.assertEqual(product_1, self.product_1)
        self.assertEqual(product_2, self.product_2)

    def test_product_print(self):
        product_1 = Products.objects.get(name="prod1")
        product_2 = Products.objects.get(name="prod2")
        self.assertEqual(str(product_1), 'prod1 cat1')
        self.assertEqual(str(product_2), 'prod2 cat1')

    def test_product_get_items(self):
        product_1 = Products.objects.get(name="prod1")
        product_3 = Products.objects.get(name="prod3")
        products = product_1.get_items()

        self.assertEqual(list(products), [product_1, product_3])
