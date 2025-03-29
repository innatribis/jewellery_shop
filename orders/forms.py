from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['last_name', 'first_name', 'second_name', 'email', 'address', 'postal_code']
