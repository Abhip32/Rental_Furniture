from sys import maxsize
from django.db import models

class Stock(models.Model):
    Product_Name=models.CharField(max_length=200,primary_key=True)
    Product_Price=models.CharField(max_length=200)
    Product_Quantity=models.CharField(max_length=200)