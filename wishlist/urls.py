from django.urls import path
from . import views

urlpatterns = [
    path('view_product_wishlist/', views.view_product_wishlist,
         name='view_product_wishlist'),
    path('add_product_to_wishlist/<item_id>/',
         views.add_product_to_wishlist, name='add_product_to_wishlist'),
    path('remove_product_from_wishlist/<item_id>/<redirect_from>/',
         views.remove_product_from_wishlist,
         name='remove_product_from_wishlist'),
]
