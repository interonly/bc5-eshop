from django import forms
from .models import *

class DatePicker(forms.DateInput):
    input_type = 'date'

class ProductForm(forms.ModelForm):
    guarantee = forms.DateField(
        widget=DatePicker,
        label="Срок гарантии",
        required=False,
    )
    expiration_date = forms.DateField(
        widget=DatePicker,
        label="Срок годности",
        required=False,
    )
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'qty',
            'category',
            'image',
            'guarantee',
            'expiration_date'
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'