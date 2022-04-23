from django.contrib import admin
from .models import Cart, Expired, Invoice,OutOfStock
from .models import Order

# Register your models here.
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Invoice)
admin.site.register(Expired)
admin.site.register(OutOfStock)
