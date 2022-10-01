from django.contrib import admin
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price']

admin.site.register(models.Collection)
