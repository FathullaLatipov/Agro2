# Generated by Django 3.2.7 on 2021-09-27 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0055_auto_20210927_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='image44',
            field=models.FileField(blank=True, null=True, upload_to='products/textures', verbose_name='image44'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='image55',
            field=models.FileField(blank=True, null=True, upload_to='products/textures', verbose_name='image55'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='image66',
            field=models.FileField(blank=True, null=True, upload_to='products/textures', verbose_name='image66'),
        ),
    ]
