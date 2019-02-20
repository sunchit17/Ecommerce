from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=850)
    price=models.FloatField()
    description=models.TextField()
    imglink=models.CharField(max_length=850)

    def __str__(self):
        return self.name

class Order(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=100)
    payment_method=models.CharField(max_length=100)
    payment_data=models.CharField(max_length=400)
    items=models.TextField()
    fulfilled=models.BooleanField()
