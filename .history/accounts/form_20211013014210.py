from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(w)
    class Meta:
        model = Account
        fields = ['first_name', 'last_name',
                  'phone_number', 'email', 'password']
