from django.urls import path
from . import views
urlpatterns = [
    path('', views.invoices, name='invoices'),
    path('add', views.add_invoice, name='add_invoice'),
    path('details/<int:pk>', views.invoice_details, name='invoice_details'),
    path('update/<int:pk>', views.update_invoice, name='edit_invoice'),
    path('delete/<int:pk>', views.delete_invoice, name='delete_invoice')
    
    ]