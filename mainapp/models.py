from django.db import models
from django.db.models import CASCADE


# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.name


#  методичка 3
class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='product_images', blank=True)
    desc = models.CharField(verbose_name='краткое описание', max_length=32,
                            blank=True)
    desc_full = models.TextField(verbose_name='полное описание', db_index=True,
                                 blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0,
                                verbose_name='цена')
    quantity = models.PositiveIntegerField(verbose_name='остаток на складе',
                                           null=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.category.name)
