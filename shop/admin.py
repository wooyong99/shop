from django.contrib import admin
from .models import *
# Register your models here.

class ProductInline(admin.TabularInline):
    model = Product
    extra = 2
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)