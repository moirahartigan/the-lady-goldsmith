from django import forms

from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

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