from django.urls import path
from .views import *

urlpatterns = [
    path('', users_list, name='users_page_url'),
    path('<str:username>/', user_detail, name='user_detail_url'),
    path('<str:username>/update/', user_detail_update, name='user_detail_update_url')
]