from django.db import models
from django.contrib.auth.models import User

loan_type_choices = (
    (1,'Home Loan'),
    (2,'Personal Loan'),
    (3,'Vehicle Loan'),
    (4,'Study Loan'),
    (5,'Others'),
)

loan_application_status = (
    (1,'Draft'),
    (2,'Submitted'),
    (3,'Approved'),
    (4,'Rejected'),
    (5,'Withdrawn'),
)

# Create your models here.
class HouseAdvertisement(models.Model):
    # each class variable represents a database i.e. table field in the model
    amount = models.IntegerField()
    tenure = models.IntegerField()
    purpose = models.CharField(max_length=2000)
    loan_type = models.IntegerField(choices=loan_type_choices)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    #status = models.IntegerField(choices=loan_application_status)
    