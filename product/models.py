from django.db import models
from django_resized import ResizedImageField

class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=100, null=True,blank=True)
    fabric_type = ResizedImageField(force_format="WEBP", upload_to="fabric/", quality=90, blank=True, null=True)
    per_meter_price = models.FloatField()
    stok = models.FloatField(default=0) 

    def __str__(self):
        return self.name


