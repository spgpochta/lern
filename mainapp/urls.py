from django.urls import path
import mainapp.views as mainapp
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'mainapp'

urlpatterns = [
    path('product/<int:pk>/', mainapp.product, name='product'),
    path('category/<int:pk>/', mainapp.products, name='category'),
    url(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/$', mainapp.products,
        name='page')
]
urlpatterns += staticfiles_urlpatterns()
