from django.contrib import admin
from catalog.models import User, Order, Product

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)