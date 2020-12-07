from django.shortcuts import render
import json
import os

# Create your views here.
JSON_PATH = 'mainapp/json/'


def json_from(file_json):
    with open(JSON_PATH + file_json, 'r', encoding='utf-8') as f:
        return json.load(f)


# в индексе передвть конткст названия загаловка сайта на заголовке
# продуктов  написано geekshop / products
def index(request):  # отрисовывает страницу по запросу
    # и отображает в ней разные данные динамически

    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)  # по такой локации


#  в прод products контекст из продуктов и отобразить в одном div продукты
def products(request):
    json_products = json_from('cloth_cadrs.json')
    context = {
        'title': 'продукты',
        'prs': json_products,
    }
    return render(request, 'mainapp/products.html', context)


def contex(request):
    context = json_from('m_cadrs.json')

    return render(request, 'mainapp/contex.html', context)
