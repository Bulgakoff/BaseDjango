from django.contrib import admin

from authapp.models import User, ShopUserProfile
from ordersapp.models import Order

admin.site.register(User)
admin.site.register(ShopUserProfile)
admin.site.register(Order)

