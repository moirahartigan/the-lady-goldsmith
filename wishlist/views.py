from django.http import Http404
from django.shortcuts import (render, get_object_or_404, redirect)
from django.contrib import messages

from django.urls import reverse


from products.models import Product
from .models import Wishlist



def view_product_wishlist(request):
    """
    A view that displays users wishlist
    Args:
        request (object): HTTP request object.
    Returns:
        Renders the request, template and context
    """
    try:
        all_wishlist = Wishlist.objects.filter(username=request.user.id)[0]
    except IndexError:
        wishlist_items = None
    else:
        wishlist_items = all_wishlist.products.all()

    if not wishlist_items:
        messages.info(request, 'Your wishlist list is empty!')

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, template, context)


def add_product_to_wishlist(request, item_id):
    """
    Add a product item to wishlist
    """
    product = get_object_or_404(Product, pk=item_id)
    try:
        wishlist = get_object_or_404(Wishlist, username=request.user.id)
    except Http404:
        wishlist = Wishlist.objects.create(username=request.user)
    if product in wishlist.products.all():
        messages.info(request, 'The product item is already in your wishlist!')
    else:
        wishlist.products.add(product)
        messages.info(request, 'Added product item to your wishlist')
    return redirect(reverse('product_detail', args=[item_id]))


def remove_product_from_wishlist(request, item_id):
    """
    Remove a product item from wishlist
    """
    product = get_object_or_404(Product, pk=item_id)
    wishlist = get_object_or_404(Wishlist, username=request.user.id)
    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.info(request, 'Product item removed from your wishlist list')
    else:
        messages.error(request, 'That product item is not in your wishlist list!')
    return redirect(reverse('product_detail', args=[item_id]))
