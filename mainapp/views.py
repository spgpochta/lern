from django.shortcuts import render
from .models import ProductCategory, Product
import logging
# from basketapp.models import Basket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import dateformat
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.conf import settings
from basketapp.models import Basket

logging.basicConfig(filename="mainapp_views.log", level=logging.DEBUG,
                    format="%(levelname)-10s %(asctime)s %(message)s")


# Create your views here.

def main(request):
    title = 'главная'
    category = ProductCategory.objects.all()
    logging.debug("категории", category)
    products = Product.objects.all()[:4]

    content = {'title': title, 'products': products, 'category': category, }
    return render(request, 'mainapp/base.html', content)


def getBasket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def products(request, pk=None, page=1):
    title = 'welcome to woodhouse'
    links_menu = ProductCategory.objects.filter(is_active=True)
    basket = []

    now = dateformat.format(datetime.now(), settings.DATE_FORMAT)

    if request.user.is_authenticated:
        basket = getBasket(request.user)

    if pk:
        if pk == '0':
            category = {'pk': 0,
                        'name': 'все продукты'}
            products_ = Product.objects.filter(
                category__is_active=True).order_by('-price')

        # is_active=True
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_ = Product.objects.filter(category__pk=pk,
                                               category__is_active=True).order_by(
                'price')

        paginator = Paginator(products_, 3)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context = {'welcome': title, 'links_menu': links_menu,
                   'category': category, 'products': products_paginator,
                   'now': now, 'basket': basket, }

        return render(request, 'mainapp/products_list.html', context)

    products_ = Product.objects.all()

    context = {'welcome': title, 'now': now, 'products': products_,
               'links_menu': links_menu, 'category': {'name': 'все продукты'},
               'basket': basket, 'Контакты': 'contact'}

    return render(request, 'mainapp/products_list.html', context)
