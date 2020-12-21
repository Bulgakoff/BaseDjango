from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from mainapp.models import ProductCategory, Products


def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    print(f'вы выбрали {pk}')
    products_db = Products.objects.all()
    links_menu = ProductCategory.objects.all()

    context = {
        'title': 'продукты',
        'prds_db': products_db,
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context)
