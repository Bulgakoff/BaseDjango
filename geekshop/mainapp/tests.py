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


