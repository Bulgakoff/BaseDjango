# Generated by Django 2.2.17 on 2021-01-15 20:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0012_auto_20210115_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 17, 20, 16, 21, 731541, tzinfo=utc)),
        ),
    ]