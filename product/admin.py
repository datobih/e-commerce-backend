from django.contrib import admin
from .models import(Product,ProductImage,
Rating,Order,OrderItem)
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Rating)
admin.site.register(Order)
admin.site.register(OrderItem)


