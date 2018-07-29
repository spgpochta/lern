#from django.urls import path
from django.conf.urls import url
import contactsapp.views as contactsapp

app_name = 'contacts'

urlpatterns = [url(r'^$', contactsapp.contact, name='contact')]
