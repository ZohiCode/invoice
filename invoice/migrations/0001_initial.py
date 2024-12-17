# Generated by Django 5.1.3 on 2024-12-13 11:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '__first__'),
        ('product', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(choices=[('KGS', 'Лв'), ('EUR', '€'), ('USD', '$'), ('TL', '₺')], default='USD', max_length=3)),
                ('rate', models.FloatField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField(default=0)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('costumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.currency')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_metre', models.FloatField(default=100)),
                ('count', models.FloatField(default=1)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.invoice')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]