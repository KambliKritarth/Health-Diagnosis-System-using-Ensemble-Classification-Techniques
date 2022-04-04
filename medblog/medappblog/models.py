from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Disease(models.Model):
    disease_name = models.CharField(max_length=255) #13:30
    
class HDSymptom(models.Model):
    age = models.IntegerField(default=0)
    anaemia = models.CharField(default = "",max_length=255)
    CreatiPhosph = models.IntegerField(default=0)
    EjectFract = models.IntegerField(default=0)
    highBP = models.CharField(default = "",max_length=255)
    SerCreat = models.IntegerField(default=0)
    SerSodiu = models.IntegerField(default=0)
    sex = models.CharField(default = "",max_length=255)
    smoking = models.CharField(default = "",max_length=255)
    followUpTime = models.IntegerField(default=0)

'''
    (done) there needs to be (default = "smth") after each .DataTypeField
    
    In heartdisease.html 
    ==> create a form with <form method = "POST">
    .
    .
    .
    </form>

    In views.py 
    ==> we will need to import HDSymptom class from theblog.models 
    ==> In function formsubmissionheartdisease:
        ==> 


'''