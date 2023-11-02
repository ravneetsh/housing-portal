from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(validators=[validators.validate_email])
    
    min_length = 2
    max_length = 40
    message_lt_min = f"Should have at least {min_length} characters."
    message_ht_max = f"Should have at most {max_length} characters."
    name_regex='\A[a-zA-Z]+\Z'
    name_message='The name accepts only letters!'

    first_name = forms.CharField(validators=[
        validators.MinLengthValidator(min_length, message_lt_min),
        validators.MaxLengthValidator(max_length, message_ht_max),
        validators.RegexValidator(name_regex, name_message)
        ])
        
    last_name = forms.CharField(validators=[
        validators.MinLengthValidator(min_length, message_lt_min),
        validators.MaxLengthValidator(max_length, message_ht_max),
        validators.RegexValidator(name_regex, name_message)
        ])
        
    contact_no = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                    error_messages = {'invalid': "Contact number must be entered in the format: '+999999999'. Maximum 15 digits are allowed."})
    
    class Meta:
        model = User
        fields = ['username', 'first_name',
        'last_name', 'contact_no', 'email', 'password1', 'password2']