from sys import maxsize
from django.db import models

class Stock(models.Model):
    Product_Name=models.CharField(max_length=200,primary_key=True)
    Product_Price=models.CharField(max_length=200)
    Product_Dis_Price=models.CharField(max_length=200)
    Product_Quantity=models.CharField(max_length=200)
    Product_Image=models.CharField(max_length=200)
    Product_Catagory=models.CharField(max_length=200)