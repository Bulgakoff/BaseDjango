# Generated by Django 2.2.17 on 2021-01-21 09:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0021_auto_20210120_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 23, 9, 7, 9, 298666, tzinfo=utc)),
        ),
    ]
