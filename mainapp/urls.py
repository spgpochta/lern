from django.urls import path
import mainapp.views as mainapp
from django.conf.urls import url


app_name = 'mainapp'

urlpatterns = [

    path('product/<int:pk>/', mainapp.products, name='product'),
    path('category/<int:pk>/', mainapp.products, name='category'),

    #url(r'^category/(?P<pk>\d+)/$', mainapp.products, name='category')
]