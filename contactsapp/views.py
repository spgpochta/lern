from django.shortcuts import render
from contactsapp.models import Contacts
from mainapp.models import ProductCategory
from datetime import datetime
from django.utils import dateformat
# from . import settings
from mainapp.views import getBasket
# Create your views here.
from django.conf import settings


def contact(request):
    locations = Contacts.objects.all().order_by('id')
    links_menu = ProductCategory.objects.all()
    now = dateformat.format(datetime.now(), settings.DATE_FORMAT)

    basket = []

    if request.user.is_authenticated:
        basket = getBasket(request.user)

    title = 'Наши адреса'
    context = {'welcome': title, 'links_menu': links_menu, 'basket': basket,
               'now': now, 'locations': locations, }
    return render(request, 'mainapp/contact.html', context)
