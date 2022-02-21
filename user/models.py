from ctypes import addressof
from django.db import models
import datetime

# Create your models here.


class Disease(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50, blank=True)
    dateOfBirth = models.DateField('Date of Birth')
    lastDateOfDonation = models.DateTimeField('Last Donation date', blank=True)
    gender = models.CharField(max_length=20)
    bloodType = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    isDonor = models.BooleanField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    donationCount = models.IntegerField(default=0)

    diseases = models.ManyToManyField(Disease, blank=True)

    def __str__(self):
        return self.name


# class hasDisease(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     diseases = models.ForeignKey(Diseases, on_delete=models.CASCADE)
#     fromDate = models.DateField('Diagnosis date')
