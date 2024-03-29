# Generated by Django 3.2.7 on 2021-09-28 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0069_auto_20210928_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='image',
            field=models.FileField(null=True, upload_to='products', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='image44',
            field=models.FileField(blank=True, null=True, upload_to='products/textures', verbose_name='image44'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='image77',
            field=models.FileField(blank=True, null=True, upload_to='products', verbose_name='image77'),
        ),
    ]
