# Generated by Django 5.1.3 on 2024-12-16 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_invoice_invoice_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceproduct',
            name='invoice_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
