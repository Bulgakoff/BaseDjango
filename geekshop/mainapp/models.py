from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='название категории', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание категории', blank=True)
    is_active = models.BooleanField(verbose_name='категория активна', db_index=True,default=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(verbose_name='название продукта', max_length=256)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    short_description = models.CharField(verbose_name='краткое описание продукта', max_length=64, blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    guantity = models.PositiveIntegerField(verbose_name='колличество продукта на складе', default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name='продукт активен',db_index=True, default=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} {self.category.name}'

    @staticmethod
    def get_items():
        # return Products.objects.filter(is_active=True).order_by('category','name')
        return Products.objects.filter(is_active=True).order_by('category','name').select_related()
