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
        self.fields['address'].validators.append(
            validators.MinLengthValidator(min_length, message_lt_min)
        )
        self.fields['number_of_bedroom'].validators.append(validators.MinValueValidator(1))
        self.fields['number_of_bathroom'].validators.append(validators.MinValueValidator(1))
        self.fields['floor_number'].validators.append(validators.MinValueValidator(-2))
        self.fields['contact_no'].validators.append(validators.RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Contact number must be entered in the format: '+999999999'.\
                            Maximum 15 digits are allowed."
            ))

    class Meta: # pylint: disable=too-few-public-methods
        '''internal meta class'''
        model = HouseAdvertisement
        fields = ['number_of_bedroom', 'number_of_bathroom', 'floor_number',
                    'nearby_utilities_landmarks', 'city', 'address',
                    'advertisement_visibility', 'contact_no']

        widgets = {
            'nearby_utilities_landmarks': forms.Textarea(),
            'address': forms.Textarea(),
            }
