from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                'street_address1', 'street_address2',
                'town_or_city', 'postcode', 'country',
                'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        # call default method to set up form as it would be by default
        super().__init__(*args, **kwargs)
        # Add placeholders to boxes
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        # Set cursor to start in full name when page loads
        self.fields['full_name'].widget.attrs['autofocus'] = True
        # Go through the list
        for field in self.fields:
            # If the field is required, add a star
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            # set placeholder values as per above
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Add the css class we haven't created yet
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Remove labels
            self.fields[field].label = False
