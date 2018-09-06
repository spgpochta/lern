from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from basketapp.models import Basket
from mainapp.models import Product
from .forms import OrderCreateForm
from .models import OrderItem
# Create your views here.


@login_required
def basket(request):
    title = 'корзина'
    basket_items = Basket.objects.filter(user=request.user).order_by('product')
    context = {'title': title, 'basket_items': basket_items}

    return render(request, 'basketapp/basket.html', context)


@login_required
def basket_add(request, pk):

    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('product', args=[pk]))

    product = get_object_or_404(Product, pk=pk)
    old_basket_item = Basket.objects.filter(user=request.user, product=product)

    if old_basket_item:
        old_basket_item[0].quantity += 1
        old_basket_item[0].save()
    else:
        new_basket_item = Basket(user=request.user, product=product)
        new_basket_item.quantity += 1
        new_basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    if request.method == 'POST':
        basket_record = get_object_or_404(Basket, pk=pk)
        basket_record.delete()
    else:
        raise Http404

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = Basket.objects.get(pk=int(pk))

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basket_items = Basket.objects.filter(user=request.user).order_by('product')

        context = {
            'basket_items': basket_items,
        }

        result = render_to_string('basketapp/includes/inc_basket_list.html', context)

        return JsonResponse({'result': result})


@login_required
def OrderCreate(request):
    cart = Basket.objects.filter(user=request.user)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'basketapp/order_created.html', {'order': order})

    form = OrderCreateForm()
    return render(request, 'basketapp/order_create.html', {'cart': cart,
                                                        'form': form})
