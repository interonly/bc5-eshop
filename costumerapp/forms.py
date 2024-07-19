from django import forms
from .models import Costumer, Profile


class CostumerForm(forms.ModelForm):
    class Meta:
        model = Costumer
        fields = [
            'name',
            'age',
            'gender',
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'bio',
            'social_link',
            'phone_number',
        ]