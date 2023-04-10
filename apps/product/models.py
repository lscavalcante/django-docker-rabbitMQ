from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    decription = models.TextField()
    price = models.DecimalField(max_digits=16, decimal_places=2)
