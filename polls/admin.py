from django.contrib import admin
from .models import Product_Chennai, Product_Bangalore, Product_Delhi, Product_Hyderabad
# Register your models here.admin.site.register
admin.site.register(Product_Chennai)
admin.site.register(Product_Delhi)
admin.site.register(Product_Hyderabad)
admin.site.register(Product_Bangalore)
