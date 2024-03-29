# Generated by Django 3.2.7 on 2021-09-28 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0064_auto_20210928_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='image22',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='image33',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='image44',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='image55',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='image66',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='image77',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='image88',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='image99',
        ),
        migrations.RemoveField(
            model_name='threedmodel',
            name='image',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(null=True, upload_to='product', verbose_name='image'),
        ),
        migrations.AddField(
            model_name='threedmodel',
            name='image22',
            field=models.FileField(blank=True, null=True, upload_to='products', verbose_name='image22'),
        ),
        migrations.AddField(
            model_name='threedmodel',
            name='image33',
            field=models.FileField(blank=True, null=True, upload_to='products', verbose_name='image33'),
        ),
        migrations.AddField(
            model_name='threedmodel',
            name='image44',
            field=models.FileField(blank=True, null=True, upload_to='products', verbose_name='image44'),
        ),
        migrations.AddField(
            model_name='threedmodel',
            name='image55',
            field=models.FileField(blank=True, null=True, upload_to='products/textures', verbose_name='image55'),
        ),
        migrations.AddField(
            model_name='threedmodel',
            name='image66',
            field=models.FileField(blank=True, null=True, upload_to='products/textures', verbose_name='image66'),
        ),
        migrations.AddField(
            model_name='threedmodel',
            name='image77',
            field=models.FileField(blank=True, null=True, upload_to='products/texture', verbose_name='image77'),
        ),
        migrations.AddField(
            model_name='threedmodel',
            name='image88',
            field=models.FileField(blank=True, null=True, upload_to='products', verbose_name='image88'),
        ),
        migrations.AddField(
            model_name='threedmodel',
            name='image99',
            field=models.FileField(blank=True, null=True, upload_to='products', verbose_name='image99'),
        ),
    ]
