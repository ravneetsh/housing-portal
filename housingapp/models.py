"""Modules defining model classes for advertisment"""
from django.db import models
from django.contrib.auth.models import User

advertisement_visibility = (
    (1,'Visible'),
    (2,'Hidden')
)

class City(models.Model):
    """Defining model class for city master"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

# Create your models here.
class HouseAdvertisement(models.Model):
    """Defining model class for advertisement"""
    # each class variable represents a database i.e. table field in the model
    rent_per_month = models.PositiveIntegerField()
    number_of_bedroom = models.PositiveIntegerField()
    number_of_bathroom = models.PositiveIntegerField()
    floor_number = models.IntegerField()
    nearby_utilities_landmarks = models.CharField(max_length=500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    advertisement_visibility = models.IntegerField(choices=advertisement_visibility)
    contact_no = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.number_of_bedroom} Bedroom, \
            {self.number_of_bathroom} Bathroom in {self.city}"