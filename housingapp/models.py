from django.db import models
from django.contrib.auth.models import User

advertisement_visibility = (
    (1,'Visible'),
    (2,'Hidden')
)

class City(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Create your models here.
class HouseAdvertisement(models.Model):
    # each class variable represents a database i.e. table field in the model
    number_of_bedroom = models.IntegerField()
    number_of_bathroom = models.IntegerField()
    floor_number = models.IntegerField()
    nearby_utilities_landmarks = models.CharField(max_length=500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    advertisement_visibility = models.IntegerField(choices=advertisement_visibility)
    