# Generated by Django 5.1.3 on 2025-03-19 10:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_articolo_datapubblicazione_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articolo',
            name='dataPubblicazione',
            field=models.DateField(blank=True, default=datetime.datetime(2025, 3, 19, 11, 33, 56, 953142)),
        ),
        migrations.AlterField(
            model_name='giornalista',
            name='dataNascita',
            field=models.DateField(blank=True, default=datetime.datetime(2025, 3, 19, 11, 33, 56, 953142)),
        ),
    ]
