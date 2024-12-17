from django.contrib import admin
from .models import Invoice, InvoiceProduct, Currency


class InvoiceProductInline(admin.TabularInline):
    model = InvoiceProduct


class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceProductInline]


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceProduct)
admin.site.register(Currency)
