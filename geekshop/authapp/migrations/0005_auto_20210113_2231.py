# Generated by Django 2.2.17 on 2021-01-13 19:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20210113_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 15, 19, 31, 10, 144709, tzinfo=utc)),
        ),
    ]
