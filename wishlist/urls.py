from django.urls import path
from . import views

urlpatterns = [
    path('view_product_wishlist/', views.view_product_wishlist, name='view_product_wishlist')
]
