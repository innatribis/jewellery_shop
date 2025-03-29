from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            order_created.delay(order.id)
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})


def order_find_num(request, fid=None):
    fid = request.GET.get('fid')
    order = Order.objects.filter(id=fid)
    if order:
        order = get_object_or_404(Order, id=fid)
    cart = OrderItem.objects.filter(order=fid)
    sum = 0
    for products in cart:
        sum+=products.price
    return render(request, 'orders/order/find.html',
                  {'order': order, 'cart': cart, 'sum':sum})
