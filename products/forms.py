from django import forms
from django.forms import Textarea

from .models import Product, Category, Review
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'name',
            'category',
            'price',
            'colour',
            'sku',
            'description',
            'has_sizes',
            'pre_sale_price',
            'image',
        )

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    # over ride the init method to make changes to the fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # Use friendly names instead of id
        self.fields['category'].choices = friendly_names
        # Add style classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductReviewForm(forms.ModelForm):
    """
    A class for product rating and comments
    """
    class Meta:
        """
        A class for fields and types for product rating and comments form.
        """
        model = Review
        fields = (
            'product_rating',
            'review_text',
        )

        widgets = {
            'product_rating': forms.Select(attrs={'id': 'product_rating'}),
            'review_text': Textarea(attrs={'rows': 3}),
        }
