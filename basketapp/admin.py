from django.contrib import admin
from.models import Basket
# Register your models here.


#расширение стандартной админки

# class BasketAdmin (admin.ModelAdmin):
#     list_display = ['product','quantity', 'user']


admin.site.register(Basket)