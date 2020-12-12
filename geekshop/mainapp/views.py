from django.shortcuts import render
from mainapp.models import ProductCategory, Products


def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    products_db = Products.objects.all()
    categories_db = ProductCategory.objects.all()

    context = {
        'title': 'продукты',
        'prds_db': products_db,
        'categs_db': categories_db,
    }
    return render(request, 'mainapp/products.html', context)
