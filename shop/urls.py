from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', product_in_category, name='product_all'),
    path('<category_id>/', product_in_category, name='product_in_category'),
    path('product/search/',product_search, name="product_search_detail"),
    path('product/<product_id>/', product_detail, name='product_detail'),
    path('product/<product_id>/payment/',product_pay, name='product_pay'),
]
