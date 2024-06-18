from django.db import models

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField
    price = models.BigIntegerField 
    # suppliers = models=
