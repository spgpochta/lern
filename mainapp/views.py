from django.shortcuts import render
from .models import ProductCategory, Product


# Create your views here.

def main(request):
    title = 'главная'
    products = Product.objects.all()[:4]
    category = ProductCategory.objects.all()
    content = {'title': title, 'products': products, 'category': category}
    return render(request, 'mainapp/base.html', content)


def products(request, pk=None):
    print(pk)

def category(request, pk=None):
    print(pk)