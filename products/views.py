from django.shortcuts import render, get_object_or_404
from .models import product

# Create your views here.

def all_products(request):
    """ all products view """

    products = product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ individual products view """
    
    product = get_object_or_404(product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)