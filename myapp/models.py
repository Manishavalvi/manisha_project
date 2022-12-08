from enum import unique
from time import time
from django.db import models

# Create your models here.


class AppoUser(models.Model):       
    
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30, null = True, blank = True)
    email = models.EmailField(unique = True)
    mobile = models.CharField(max_length=15)
    date = models.CharField(max_length = 25)
    time = models.CharField(max_length = 25)

    def __str__(self):  
        return self.email

class Doctor(models.Model):
    
    d_name = models.CharField(max_length=30)
    speciality = models.CharField(max_length=30)
    pic = models.FileField(upload_to='doctor',default='')
    description = models.CharField(max_length=350)
    def __str__(self):
        return self.d_name

class Contact(models.Model):
    
    full_name = models.CharField(max_length=30)
    email = models.EmailField(unique = True)
    subject = models.CharField(max_length=30)
    message = models.CharField(max_length=30)
    
    def __str__(self):
        return self.full_name

