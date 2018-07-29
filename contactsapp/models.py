from django.db import models
# Create your models here.

class Contacts(models.Model):
    name = models.CharField(verbose_name='Метка офиса', max_length=128, unique=True)
    city = models.CharField(verbose_name='Город/населенный пункт', max_length=128, unique=False)
    phone = models.CharField(verbose_name='Телефонама', max_length=32, unique=True)
    email = models.CharField(verbose_name='Почтанама', max_length=32, unique=True)
    address = models.CharField(verbose_name='Полный адрес', max_length=128, unique=False)
    
    
    def __str__ (self): return self.name