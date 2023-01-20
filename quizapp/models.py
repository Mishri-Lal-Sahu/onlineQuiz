from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField(max_length=50)
    uname=models.CharField(max_length=50)
    password=models.CharField(max_length=20)