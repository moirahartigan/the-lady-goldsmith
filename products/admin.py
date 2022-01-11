from django.contrib import admin
from .models import Product, Category, Review


class ProductAdmin(admin.ModelAdmin):
    """
    Admin class for the Product model.
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'pre_sale_price',
        'rating',
        'image',
        'image_url',
    )
    list_filter = (
        'sku',
        'category',
        'name',
        'price',
    )
    search_fields = (
        'sku',
        'category',
        'name',
        'price',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin class for the Category model.
    """
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    """
    Admin class for the Review model.
    """
    list_display = (
        'review_text',
        'product_rating',
    
    )
    


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)


