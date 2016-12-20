

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Product_Category,Product,Blog,News,Research,Research_TimeLine,Order

admin.site.register(Product_Category)
admin.site.register(Product)
admin.site.register(Blog)
admin.site.register(News)
admin.site.register(Research)
admin.site.register(Research_TimeLine)
admin.site.register(Order)