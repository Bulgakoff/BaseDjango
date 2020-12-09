from django.shortcuts import render
import json
from mainapp.models import ProductCategory, Products



JSON_PATH = 'mainapp/json/'


def json_from(file_json):
    with open(JSON_PATH + file_json, 'r', encoding='utf-8') as f:
        return json.load(f)



def index(request):

    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    json_products = json_from('cloth_cadrs.json')
    products_db = Products.objects.all()
    context = {
        'title': 'продукты',
        'prs': json_products,
        'prds_db': products_db,
    }
    return render(request, 'mainapp/products.html', context)


def contex(request):
    context = json_from('m_cadrs.json')

    return render(request, 'mainapp/contex.html', context)


def new(request):
    ppp = Products.objects.all()
    context = {
        'title': 'главная',
        'prds': ppp,
    }
    return render(request, 'mainapp/new.html', context)
