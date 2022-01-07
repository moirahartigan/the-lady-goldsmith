from django.shortcuts import render

from django.contrib import messages

from django.urls import reverse


from products.models import Product
from util.util import setup_pagination
from .models import Wishlist



def view_product_wishlist(request):
    """
    A view that displays users wishlist
    Args:
        request (object): HTTP request object.
    Returns:
        Renders the request, template and context
    """
    wishlist_items_count = 0
    try:
        all_wishlist = Wishlist.objects.filter(username=request.user.id)[0]
    except IndexError:
        wishlist_items = None
    else:
        wishlist_items = all_wishlist.products.all()
        wishlist_items_count = all_favourites.products.all().count()
        wishlist_items = setup_pagination(favourites_items, request, 4)

    if not wishlist_items:
        messages.info(request, 'Your wishlist list is empty!')

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist_items': wishlist_items,
        'wishlist_items_count': wishlist_items_count
    }
    return render(request, template, context)
