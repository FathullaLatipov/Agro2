# Generated by Django 3.2.7 on 2021-09-28 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0067_auto_20210928_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='image',
        ),
    ]
