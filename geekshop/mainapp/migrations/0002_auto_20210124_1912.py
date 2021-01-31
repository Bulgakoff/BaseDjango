# Generated by Django 2.2.17 on 2021-01-24 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='description',
            field=models.TextField(blank=True, verbose_name='описание категории'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='категория активна'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='название категории'),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True, verbose_name='описание продукта'),
        ),
        migrations.AlterField(
            model_name='products',
            name='guantity',
            field=models.PositiveIntegerField(default=0, verbose_name='колличество продукта на складе'),
        ),
        migrations.AlterField(
            model_name='products',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='продукт активен'),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=256, verbose_name='название продукта'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='цена продукта'),
        ),
        migrations.AlterField(
            model_name='products',
            name='short_description',
            field=models.CharField(blank=True, max_length=64, verbose_name='краткое описание продукта'),
        ),
    ]