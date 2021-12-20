from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    # if bag is empty
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        # redirect back to the checkout page 
        return redirect(reverse('products'))

    # create empty instance of order form 
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JxVZlDaCUI9Xs6pYLpQtpPpwXkajedKGkISekzYYszDhKvkXREIGFq08YyaESkDZBXk0dGlkjwVb5wmpkeSeRR000aaxfuiCJ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
