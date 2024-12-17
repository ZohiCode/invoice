from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number  = models.CharField(max_length=13)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name