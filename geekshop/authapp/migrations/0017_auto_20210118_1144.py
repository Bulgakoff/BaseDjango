# Generated by Django 2.2.17 on 2021-01-18 08:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0016_auto_20210118_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 20, 8, 44, 27, 198297, tzinfo=utc)),
        ),
    ]
