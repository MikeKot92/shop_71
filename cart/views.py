from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages


from products.models import Product

from .models import Cart


@login_required
def cart(request):
    context = {
        'title': 'Cart',
    }
    return render(request, 'cart.html', context)


@login_required
def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)
    carts = Cart.objects.filter(user=request.user, product=product)
    if not carts.exists():
        Cart.objects.create(user=request.user, product=product, quantity=1)
        messages.success(request, f"Товар  добавлен в корзину!")
    else:
        cart = carts.first()
        cart.quantity += 1
        cart.save()
        messages.success(request, f"Товар  добавлен в корзину!")
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
