from .models import InvoiceProduct, Invoice
from django import forms

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['costumer', 'total_price', 'date_time']


class InvoiceProductForm(forms.ModelForm):
    class Meta:
        model = InvoiceProduct
        fields = ['product', 'total_metre', 'count']

