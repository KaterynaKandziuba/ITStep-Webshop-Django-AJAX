from django.contrib import admin
from .models import Order, Order_C

admin.site.register(Order_C)
admin.site.register(Order)
