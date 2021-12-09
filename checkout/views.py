from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        message.error(request, "Basket Empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K4VeCDqyFPPd75kGeX2aroUsnYjKaNg3yl07WVlXrM1XZ8KL1Y1nxJesFP5szKAB6kbsJLosPXnScXCUQlrxuEM00NlSj8HHr',
        'client_secret': 'test client secret'
    }   

    return render(request, template, context)