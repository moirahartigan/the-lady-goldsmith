from django import forms


class Contact(forms.Form):

    name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    message = forms.CharField(required=True)