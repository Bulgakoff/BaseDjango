from django.db import connection
from django.db.models import F
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from mainapp.models import Products
from basketapp.models import Basket
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse


@login_required
def basket_add(request, id_product=None):
    product = get_object_or_404(Products, id=id_product)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        basket = Basket(user=request.user, product=product)
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        # """
        # UPDATE "basketapp_basket"
        # SET
        # "user_id" = 1,
        # "product_id" = 10,
        # "quantity" = 2,------>(# "quantity" = ("basketapp_basket"."quantity" - 1),)
        # "created_timestamp" = \'2021-02-09 10:26:11.886372\'
        # WHERE
        # "basketapp_basket"
        # """

        basket = baskets.first()
        # basket.quantity += 1
        basket.quantity = F('quantity') + 1
        basket.save()
        print(f'-=-=-=-=-=-{connection.queries}')
        update_queries = list(filter(lambda x: 'UPDATE' in x['sql'], connection.queries))
        print(f'query basket_app xxx---+++++*****++++++-> {update_queries}')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, id=None):
    # basket = Basket.objects.get(id=id)
    basket = get_object_or_404(Basket, id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, id, quantity):
    print(request)
    if request.is_ajax():
        quantity = int(quantity)
        basket = Basket.objects.get(id=int(id))
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        baskets = Basket.objects.filter(user=request.user)
        contex = {
            'baskets': baskets,
        }
        result = render_to_string('basketapp/basket.html', contex)
        # result = render_to_string('basketapp/basket.html')
        return JsonResponse({'result': result})
