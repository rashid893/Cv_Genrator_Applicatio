from math import degrees
from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=44)
    email=models.CharField(max_length=44)
    phone=models.CharField(max_length=44)
    summary=models.TextField(max_length=1184)
    degree=models.CharField(max_length=44)
    school=models.CharField(max_length=44)
    university=models.CharField(max_length=44)
    previous=models.TextField(max_length=1244)
    skills=models.TextField(max_length=1244)
    def __str__ (self):
         return self.name