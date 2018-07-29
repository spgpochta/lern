from django.urls import path
import mainapp.views as mainapp

app_name = 'products'

urlpatterns = [
    #path('/', mainapp.products, name='index'),
    path('product/<int:pk>/', mainapp.products, name='product'),
    path('category/(<int:pk>)/page/(<int:page>)/', mainapp.products,
         name='page'),
]