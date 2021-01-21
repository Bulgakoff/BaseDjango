def get_context_data(self, **kwargs):
    data = super(OrderItemsCreate, self).get_context_data(**kwargs)
    OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)

    if self.request.POST:
        formset = OrderFormSet(self.request.POST)
    else:
        basket_items = Basket.get_items(self.request.user)
        if len(basket_items):
            OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=len(basket_items))
            formset = OrderFormSet()
            for num, form in enumerate(formset.forms):
                form.initial['product'] = basket_items[num].product
                form.initial['quantity'] = basket_items[num].quantity
            basket_items.delete()
        else:
            formset = OrderFormSet()

    data['orderitems'] = formset
    return data