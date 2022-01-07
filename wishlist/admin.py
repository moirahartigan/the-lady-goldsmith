from django.contrib import admin

from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'username',
    )


admin.site.register(Wishlist, WishlistAdmin)
