from django.shortcuts import render
from products.models import Product


def index(request):
    """ A View to return the index page """

    shop_home = Product.objects.all()

    context = {
        'shop_home': shop_home,
    }
    return render(request, 'home/index.html')
