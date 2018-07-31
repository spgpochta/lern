from django.conf.urls import url
from django.urls import path
import basketapp.views as basketapp

app_name = 'basket'

urlpatterns = [

    url(r'^$', basketapp.basket, name='view'),

    path('add/<int:pk>/', basketapp.basket_add, name='add'),
    url(r'^remove/(?P<pk>\d+)/$', basketapp.basket_remove, name='remove'),
    url(r'^edit/(?P<pk>\d+)/(?P<quantity>\d+)/$', basketapp.basket_edit,
        name='edit')
]


# path('add/<int:pk>/', basketapp.basket_add, name='add'),
