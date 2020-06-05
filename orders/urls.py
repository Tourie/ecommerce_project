from django.urls import path
from .views import *

urlpatterns = [
    path('', orders_list_view, name='orders_list_url'),
]