from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    contact_no = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                    error_messages = {'invalid': "Contact number must be entered in the format: '+999999999'. Maximum 15 digits are allowed."})
    
    class Meta:
        model = User
        fields = ['username', 'first_name',
        'last_name', 'contact_no', 'email', 'password1', 'password2']