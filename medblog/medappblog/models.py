from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Disease(models.Model):
    disease_name = models.CharField(max_length=255) #13:30
    
class HDSymptom(models.Model):
    age = models.IntegerField
    anaemia = models.CharField
    CreatiPhosph = models.IntegerField
    anaemia = models.CharField
    EjectFract = models.IntegerField
    highBP = models.CharField
    SerCreat = models.IntegerField
    SerSodiu = models.IntegerField
    sex = models.CharField
    smoking = models.CharField
    followUpTime = models.IntegerField
