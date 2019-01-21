from django.shortcuts import render
from shop_temp.models import *


def homepage(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    ctx = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'home.html', ctx)


def product_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    ctx = {
        'product': product
    }

    return render(request, 'product.html', ctx)


def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    ctx = {
        'category': category
    }

    return render(request, 'category.html', ctx)
