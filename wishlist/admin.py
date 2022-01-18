from django.contrib import admin

from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'username',
    )
    search_fields = (
        'username',
    )
    list_filter = (
        'username',
    )
    list_per_page = 20


admin.site.register(Wishlist, WishlistAdmin)
