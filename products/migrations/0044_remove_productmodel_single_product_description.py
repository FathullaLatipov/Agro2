# Generated by Django 3.2.6 on 2021-08-23 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0043_productmodel_single_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='single_product_description',
        ),
    ]
