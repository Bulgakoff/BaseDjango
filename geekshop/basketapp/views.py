from django.shortcuts import HttpResponseRedirect, get_object_or_404
from mainapp.models import Products
from basketapp.models import Basket


def basket_add(request, id_product=None):
    product = get_object_or_404(Products, id=id_product)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        basket = Basket(user=request.user, product=product)
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, id=None):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# def baskete(request, id=None):
#     basket = Basket.objects.get(id=id)
#     basket.delete()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))