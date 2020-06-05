
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
    items, num = [], 0
    try:
        items = Item.objects.filter(shop__title__iexact=title)
        num = items.count()
    finally:
        return render(request, 'shops/shop_detail.html', context={'shop': shop, 'items': items, 'num':num})


def item_detail_view(request, title):
    try:
        item = Item.objects.get(title__iexact=title)
    except Item.DoesNotExist:
        return render(request, 'errors/error.html')
    try:
        image = ItemImage.objects.get(item__title__iexact=item.title)
        return render(request, 'shops/item_detail.html', context={'item': item, 'item_image': image.image})
    except ItemImage.DoesNotExist:
        return render(request, 'shops/item_detail.html', context={'item': item})

# Create your views here.
