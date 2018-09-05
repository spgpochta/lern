from django.db import models
from mainapp.models import Product
from django.conf import settings
from django.db.models import CASCADE

# Create your models here.


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество',
                                           default=0)
    add_datetime = models.DateTimeField(verbose_name='время добавления',
                                        auto_now_add=True)

    def get_product_cost(self):
        return self.product.price * self.quantity

    def get_totalquantity(self):
        items = Basket.objects.filter(user=self.user)
        totalquantity = sum(item.quantity for item in items)
        return totalquantity

    def get_totalcost(self):
        items = Basket.objects.filter(user=self.user)
        totalquantity = sum(item.product.price*item.quantity for item in items)
        return totalquantity


class Order(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(verbose_name='Адрес', max_length=250)
    postal_code = models.CharField(verbose_name='Почтовый код', max_length=20)
    city = models.CharField(verbose_name='Город', max_length=100)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    paid = models.BooleanField(verbose_name='Оплачен', default=False)
    closed = models.DateTimeField(verbose_name='Закрыт', auto_now_add=False)
    canseled = models.DateTimeField(verbose_name='Отменён', auto_now_add=True)

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ: {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='Цена',
                                max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество',
                                           default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
