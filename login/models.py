from django.db import models

# Create your models here.
class Adduser(models.Model):
    username= models.CharField(max_length=300,primary_key=True)
    Password=models.CharField(max_length=100)
    Fname=models.CharField(max_length=50)
    Lname=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    Phone_No=models.CharField(max_length=10)
    Email=models.CharField(max_length=100)
    
