from django.shortcuts import render, redirect, get_object_or_404
from invoice.models import Invoice, InvoiceProduct
from product.models import Product
from invoice.forms import InvoiceForm, InvoiceProductForm
from django.forms import inlineformset_factory
from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO



def invoices(request):
    invoices = Invoice.objects.all().order_by('-id')
    return render(request, 'invoices.jinja.html', {'invoices': invoices})

def invoice_details(request, pk):
    invoice = get_object_or_404(Invoice, id=pk)
    invoice_products = InvoiceProduct.objects.filter(invoice=invoice).order_by('-id')
    return render(request, 'detail.jinja.html', {'invoice_products': invoice_products, 'invoice': invoice})

def add_invoice(request):
    Formset = inlineformset_factory(Invoice, InvoiceProduct, form=InvoiceProductForm, extra=1)
    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST)
        formset = Formset(request.POST)
        if invoice_form.is_valid() and formset.is_valid():
            invoice = invoice_form.save()
            formset.instance = invoice
            formset.save()
            return redirect('invoices')
        else:
            return render(request, 'add.jinja.html', {'form': invoice_form, 'formset': formset})
    else:
        form = InvoiceForm()
        formset = Formset()
    return render(request, 'add.jinja.html', {'form': form, 'formset': formset})


def update_invoice(request, pk):
    invoice = get_object_or_404(Invoice, id=pk)
    Formset = inlineformset_factory(Invoice, InvoiceProduct, form=InvoiceProductForm, extra=1)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        formset = Formset(request.POST, instance=invoice)
        if form.is_valid() and formset.is_valid():
            invoice = form.save()
            formset.instance = invoice
            formset.save()
            return redirect('invoices')
        else:
            return render(request, 'update.jinja.html', {'form': form, 'formset': formset})
    else:
        form = InvoiceForm(instance=invoice)
        formset = Formset(instance=invoice)
    return render(request, 'update.jinja.html', {'form': form, 'formset': formset})


def delete_invoice(request, pk):
    invoice = get_object_or_404(Invoice, id=pk)
    invoice.delete()
    return redirect('invoices')
