from django.db import models
from mainapp.models import Product
from django.conf import settings

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
