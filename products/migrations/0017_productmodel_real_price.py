# Generated by Django 3.2.5 on 2021-07-21 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20210719_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='real_price',
            field=models.FloatField(default=0, verbose_name='real price'),
        ),
    ]
