from django import forms
from django.forms import ModelForm
from .models import HouseAdvertisement

class HouseAdvertisementForm(ModelForm):
    class Meta:
        model = HouseAdvertisement
        #fields = '__all__'
        exclude = ["user"]
        
        widgets = {
            'nearest_landmark': forms.Textarea()
            }