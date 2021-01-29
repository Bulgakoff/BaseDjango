from django import forms

from mainapp.models import Products
from ordersapp.models import Order, OrderItems


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('user',)  # оставляем пользователя анонимным

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class OrderItemForm(forms.ModelForm):
    price = forms.CharField(label='цена', required=False)

    class Meta:
        model = OrderItems
        exclude = ()  # исключать ничего н надо используем все поля

    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

        self.fields['product'].queryset = Products.get_items()
