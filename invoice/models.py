from django.db import models
from customer.models import Customer
from product.models import Product
import random
import string

class InvoiceProduct(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    total_metre = models.FloatField(default=100)
    count = models.IntegerField(default=1)
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f'{self.product.code} - > {self.invoice.costumer.name}'
    @property
    def total_price(self):
        return self.total_metre * self.product.per_meter_price

class Currency(models.Model):
    currency ={
        "USD": '$',
        "EUR": '€',
        "KGS": 'Лв',
        "TL": '₺'
    }
    code = models.CharField(max_length=3, choices=currency,default='USD')
    rate = models.FloatField(default=1) 
    def __str__(self):
        return f'{self.code} : {self.rate}'

class Invoice(models.Model):
    costumer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    total_price = models.FloatField(default=0 , blank=True, null=True)
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE,blank=True, null=True)
    date_time = models.DateTimeField()
    invoice_number = models.CharField(max_length=6, unique=True, blank=True)
    def __str__(self):
        return f'{self.costumer.name} - > {self.total_price}'

    def save(self, *args, **kwargs):    
        if not self.invoice_number:
            self.invoice_number = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        super().save(*args, **kwargs)
    @property
    def total_invoice_price(self):
        return sum([item.total_price for item in self.invoiceproduct_set.all()])

    @property
    def total_metre(self):
        return sum([item.total_metre*item.count for item in self.invoiceproduct_set.all()])


        

