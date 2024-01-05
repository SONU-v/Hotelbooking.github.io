import datetime
from django.db import models


class Customer(models.Model):
        checkin = models.DateField()
        checkout = models.DateField()
        name = models.CharField (max_length=50)
        age = models.IntegerField()
        person = models.IntegerField()
        phone1 = models.IntegerField()
        phone2 =models.IntegerField()
        email = models.CharField(max_length=10)
        address = models.CharField(max_length=20)
        gender = models.CharField(max_length=5)
        selectcity= models.CharField(max_length=10)
        selectstate= models.CharField(max_length=10)











