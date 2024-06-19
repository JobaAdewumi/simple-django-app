from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=11)