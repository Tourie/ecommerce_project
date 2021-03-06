from django.urls import path, include

from .views import *

urlpatterns = [
    path('', shops_list_view, name='shops_list_url'),
    path('<str:title>/', shop_detail_view, name='shop_detail_url'),
    path('items/<str:title>/', item_detail_view, name='item_detail_url')
]