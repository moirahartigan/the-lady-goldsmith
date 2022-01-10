from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Wishlist


def wishlist_contents(request):
    """
    A context for Wishlist to display count in users navbar
    """
    try:
        wishlist = get_object_or_404(Wishlist, username=request.user.id)
        wishlist_items = wishlist.products.all()
        wishlist_count = len(wishlist_items)
    except Http404:
        wishlist_count = None

    context = {
        'wishlist_count': wishlist_count,
    }

    return context
