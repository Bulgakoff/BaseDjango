from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.views.decorators.cache import cache_page

from mainapp.models import ProductCategory, Products
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu=cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.filter(is_active=True)
            cache.set(key, links_menu)
        return links_menu


    else:
        return ProductCategory.objects.filter(is_active=True)

def get_category(pk):
    if settings.LOW_CACHE:
        key = f'category_{pk}'
        category = cache.get(key)
        if category is None:
            category= ProductCategory.objects.get(pk=pk)
            cache.set(key,category)
        return category

    else:
        return ProductCategory.objects.get(pk=pk)



def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)

@cache_page(3600)
def products(request, category_id=None, page=1):
    """Without pagination."""
    context = {'title': 'продукты -  КАТЕГОРИИ',
               # 'links_menu': ProductCategory.objects.all(),
               'links_menu': get_links_menu(),
               }
    if category_id:
        print(f'вы выбрали {category_id}')
        # products = Products.objects.filter(category_id=category_id).order_by('price')
        category = get_category(category_id)
        products = Products.objects.filter(is_active=True, category__is_active=True, category__pk=category_id).select_related(
            'category').order_by('price')
        # context.update({'products': products})
    else:
        # products = Products.objects.all().order_by('price')
        products = Products.objects.filter(is_active=True, category__is_active=True).select_related(
            'category').order_by('price')
        # context.update({'products': products})
    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context.update({'products': products_paginator})

    return render(request, 'mainapp/products.html', context)
