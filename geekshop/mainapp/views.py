from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from mainapp.models import ProductCategory, Products
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None, page=1):
    """Without pagination."""
    context = {'title': 'продукты -  КАТЕГОРИИ',
               'links_menu': ProductCategory.objects.all(), }
    if category_id:
        print(f'вы выбрали {category_id}')
        # products = Products.objects.filter(category_id=category_id).order_by('price')
        products = Products.objects.filter(is_active=True, category__is_active=True, category_id=category_id).order_by(
            'price')
        # context.update({'products': products})
    else:
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
