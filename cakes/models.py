from django.db import models

class CakeStock(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()

# Create your models here.
