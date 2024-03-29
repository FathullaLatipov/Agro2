# Generated by Django 3.2.7 on 2021-09-28 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0066_delete_threedmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='image22',
            field=models.FileField(blank=True, null=True, upload_to='products', verbose_name='image22'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='image33',
            field=models.FileField(blank=True, null=True, upload_to='products', verbose_name='image33'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='image44',
            field=models.FileField(blank=True, null=True, upload_to='products/textures', verbose_name='image44'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='image55',
            field=models.FileField(blank=True, null=True, upload_to='products/textures', verbose_name='image55'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='image66',
            field=models.FileField(blank=True, null=True, upload_to='products/textures', verbose_name='image66'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='image77',
            field=models.FileField(blank=True, null=True, upload_to='products', verbose_name='image77'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='image88',
            field=models.FileField(blank=True, null=True, upload_to='products', verbose_name='image88'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='image99',
            field=models.FileField(blank=True, null=True, upload_to='products', verbose_name='image99'),
        ),
    ]
