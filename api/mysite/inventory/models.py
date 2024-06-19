from django.db import models


class Inventory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.BigIntegerField()
    suppliers = models.ManyToManyField(to='supplier.Supplier')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
