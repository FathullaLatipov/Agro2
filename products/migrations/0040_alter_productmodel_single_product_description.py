# Generated by Django 3.2.6 on 2021-08-23 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0039_auto_20210823_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='single_product_description',
            field=models.TextField(verbose_name='single_product_description'),
        ),
    ]
