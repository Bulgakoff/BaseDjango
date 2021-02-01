from basketapp.models import Basket


def basket(request):
    print(f'context processor basket works')
    basket_item = []

    if request.user.is_authenticated:
        basket_item = Basket.objects.filter(user=request.user).order_by('product__category')
        # basket_item = Basket.objects.filter(user=request.user).order_by('product__category').select_related()
    return {
        'baskets': basket_item,
    }
