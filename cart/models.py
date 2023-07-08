from django.db import models
from more_itertools import quantify
from numpy import product


# Create your models here.
class Cart(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    price = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    User = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)

class Order(models.Model):
    id=models.CharField(max_length=200,primary_key=True)
    img=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    productname=models.CharField(max_length=200)
    dateoforder=models.CharField(max_length=200)
    dateofdelivery=models.CharField(max_length=200)
    placeofsender=models.CharField(max_length=200)
    placeofreceiver=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    dateofreturn=models.CharField(max_length=200)
    progress=models.CharField(max_length=200)

class Invoice(models.Model):
    id=models.CharField(max_length=200)
    url=models.CharField(max_length=200,primary_key=True)

class Expired(models.Model):
    id=models.CharField(max_length=200,primary_key=True)
    user=models.CharField(max_length=200)
    productname=models.CharField(max_length=200)
    address=models.CharField(max_length=200)

class OutOfStock(models.Model):
    id=models.CharField(max_length=200,primary_key=True)
    Catagory=models.CharField(max_length=200)