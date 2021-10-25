from django.shortcuts import render
from django.http import JsonResponse
from .models import Order_C


def ajax_cart(request):
    response = dict()
    uid = request.GET.get('uid')
    pid = request.GET.get('pid')  # забрали айдишки юзера и продукта

    Order_C.objects.create(
        title=f'Order-{pid}/{uid}',
        product_id=pid,
        user_id=uid,
        status='pending',
        amount=1
    )

    print('Hello2')
    user_orders = Order_C.objects.filter(user_id=uid)
    cost = 0
    print(cost)
    for order in user_orders:
        print(order.product.price)
        cost += order.product.price

    response['cost'] = cost
    response['count'] = len(user_orders)
    return JsonResponse(response)
