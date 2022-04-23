from django.db import models

# Create your models here.
class OTPSTORAGE(models.Model):
    password= models.CharField(max_length=50,primary_key=True)
    user=models.CharField(max_length=50)

