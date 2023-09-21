from django.contrib import admin
from .models import category, sub_category, products, brands
# Register your models here.

admin.site.register(category)
admin.site.register(sub_category)
admin.site.register(products)
admin.site.register(brands)
