from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def product_in_category(request, category_id=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_id:
        current_category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=current_category)
    return render(request, 'shop/list.html', {'current_category':current_category,
                                              'categories':categories,
                                              'products':products})

def product_detail(request, product_id=None):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/detail.html', {'product':product})
def product_search(request):
    if request.POST:
        val = request.POST['srch']
        current_product = Product.objects.get(name__startswith=val)
    return render(request, 'shop/detail.html', {'product':current_product})
def product_pay(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/payment.html', {'product':product})

