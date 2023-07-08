from sys import maxsize
from django.db import models

class Stock(models.Model):
    Product_Name=models.CharField(max_length=200,primary_key=True)
    Product_Price=models.IntegerField()
    Product_Dis_Price=models.IntegerField()
    Product_Quantity=models.IntegerField()
    Product_Image=models.CharField(max_length=200)
    Product_Catagory=models.CharField(max_length=200)


#class Cart(models.Model):
#    pName=models.CharField(max_length=200)
#    pImg=models.CharField(max_length=200)
#    pPrice=models.CharField(max_length=200)
#    p=models.CharField(max_length=200)

# Create your models here.
