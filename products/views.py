from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.

def all_products(request):
    """ all products view """

    products = Product.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    
    context = {
        'products': products,
        'current_category': categories,
        'from_gym_equipment': True,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ individual products view """
    
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def pt(request):
    """ personal trainer view"""

    return render(request, 'products/pt.html')


def nutrition(request):
    """ Nutrition view"""

    products = Product.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    
    context = {
        'products': products,
        'current_category': categories,
        'from_nutritions': True,
    }

    return render(request, 'products/nutrition.html', context)



def gymgear(request):
    """ Gym Gear view"""

    return render(request, 'products/gymgear.html')