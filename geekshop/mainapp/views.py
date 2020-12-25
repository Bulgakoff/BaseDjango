from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from mainapp.models import ProductCategory, Products
from  django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None):
    context = {
        'title': 'продукты -  КАТЕГОРИИ',
        'links_menu': ProductCategory.objects.all(),
    }
    if category_id:
        print(f'вы выбрали {category_id}')
        products = Products.objects.filter(category_id=category_id)
        context.update({'products': products})
    else:
        context.update({'products': Products.objects.all()})

    return render(request, 'mainapp/products.html', context)
