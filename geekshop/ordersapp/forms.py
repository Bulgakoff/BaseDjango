from django import forms

from ordersapp.models import Order, OrderItems


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('user',)# оставляем пользователя анонимным

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItems
        exclude = () # исключать ничего н надо используем все поля

    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'