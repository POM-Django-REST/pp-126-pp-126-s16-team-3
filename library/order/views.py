from django.shortcuts import render
from .models import Order

def index(request):
    # Сортировка по id по умолчанию
    sort_by = request.GET.get('sort', 'id')
    order_by = request.GET.get('order', 'asc')
    ordering = '-' + sort_by if order_by == 'desc' else sort_by

    orders = Order.objects.all().order_by(ordering)
    context = {
        'orders': orders,
        'current_sort': sort_by,
        'current_order': order_by,
    }
    return render(request, 'order/index.html', context)

def single_order(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return render(request, 'order/404.html', {'order_id': order_id})
    return render(request, 'order/single_order.html', {'order': order})