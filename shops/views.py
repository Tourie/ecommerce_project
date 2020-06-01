from django.shortcuts import render, redirect
from .models import *


def shops_list_view(request):
    shops_list = Shop.objects.all()
    return render(request, 'shops/shops_list.html', context={'shops_list': shops_list, 'clicked_shops': 'active'})


def shop_detail_view(request, title):
    try:
        shop = Shop.objects.get(title__iexact=title)
    except Shop.DoesNotExist:
        return render(request, 'errors/error.html')
    items, num = [],0
    try:
        items = Item.objects.filter(shop__title__iexact=title)
        num = items.count()
    finally:
        return render(request, 'shops/shop_detail.html', context={'shop': shop, 'items': items, 'num':num})

# Create your views here.
