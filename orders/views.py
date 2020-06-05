from django.shortcuts import render, redirect
from .models import Order


def orders_list_view(request):
    if not request.user.is_authenticated:
        return redirect('login_url')
    orders_list = Order.objects.filter(user__username__iexact=request.user.username)
    return render(request, 'orders/orders_list.html', context={'orders_list': orders_list, 'clicked_orders': 'active'})

# Create your views here.
