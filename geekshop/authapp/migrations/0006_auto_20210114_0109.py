# Generated by Django 2.2.17 on 2021-01-13 22:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20210113_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 15, 22, 9, 51, 800835, tzinfo=utc)),
        ),
    ]
