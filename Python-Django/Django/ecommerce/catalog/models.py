from django.db import models

 # for creating random order id
from django.utils.crypto import get_random_string

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(get_random_string(10))