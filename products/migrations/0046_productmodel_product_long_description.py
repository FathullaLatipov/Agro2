# Generated by Django 3.2.6 on 2021-08-29 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0045_remove_productmodel_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='product_long_description',
            field=models.TextField(max_length=30, null=True, verbose_name='product_long_description'),
        ),
    ]
