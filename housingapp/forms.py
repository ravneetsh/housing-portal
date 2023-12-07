'''forms definition for advertisements'''
from django import forms
from django.forms import ModelForm
from django.core import validators
from .models import HouseAdvertisement


class HouseAdvertisementForm(ModelForm):
    '''main class advertisements form'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        min_length = 5
        message_lt_min = f"Should have at least {min_length} characters."

        self.fields['nearby_utilities_landmarks'].validators.append(
            validators.MinLengthValidator(min_length, message_lt_min)
        )
        self.fields['number_of_bedroom'].validators.append(validators.MinValueValidator(1))
        self.fields['floor_number'].validators.append(validators.MinValueValidator(-2))

    class Meta: # pylint: disable=too-few-public-methods
        '''internal meta class'''
        model = HouseAdvertisement
        #fields = '__all__'
        exclude = ["user"]

        widgets = {
            'nearby_utilities_landmarks': forms.Textarea()
            }
