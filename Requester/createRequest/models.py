from django.db import models


# Each request is connected to exactly one user
# A user can have many requests
#      many            one
# User -------------------- Request
class Request(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100, blank=True)
    blood_type = models.CharField(max_length=10)
    urgency = models.CharField(max_length=10)
    prescription_link = models.CharField(max_length=100)
    date = models.DateField('Required within')

    def __str__(self):
        return self.name + " --- " + self.blood_type + " --- " + self.urgency
