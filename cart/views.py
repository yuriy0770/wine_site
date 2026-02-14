from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, CartItem


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    context = {
        'cart': cart,
        'items': cart.items.all(),
        'total': cart.get_total_price(),
        'total_quantity': cart.get_total_quantity(),
    }
    return render(request, 'cart/cart_detail.html', context)


@login_required
def cart_update(request, product_id):
    if request.method == 'POST':
        count = int(request.POST.get('count', 1))
        cart = get_object_or_404(Cart, user=request.user)
        cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)

        if count > 0:
            cart_item.count = count
            cart_item.save()
            messages.success(request, 'Количество обновлено')
        else:
            cart_item.delete()
            messages.success(request, 'Товар удален из корзины')

    return redirect('cart:detail')


@login_required
def cart_remove(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    cart_item.delete()
    messages.success(request, 'Товар удален из корзины')
    return redirect('cart:detail')


@login_required
def cart_clear(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart.items.all().delete()
    messages.success(request, 'Корзина очищена')
    return redirect('cart:detail')


@login_required
def cart_add(request, product_id):
    """Добавление товара в корзину"""
    if request.method == 'POST':
        count = int(request.POST.get('count', 1))
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, item_created = CartItem.objects.get_or_create(
            cart=cart,
            product_id=product_id,
            defaults={'count': count}
        )

        if not item_created:
            cart_item.count += count
            cart_item.save()
            message = f'Количество товара обновлено (+{count})'
        else:
            message = 'Товар добавлен в корзину'

        messages.success(request, message)

    return redirect(request.META.get('HTTP_REFERER', 'main:index'))