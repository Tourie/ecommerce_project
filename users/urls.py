from django.urls import path
from .views import *

urlpatterns = [
    path('', users_list, name='users_list_url'),
    path('<str:username>/', user_detail_view, name='user_detail_url'),
    path('<str:username>/update/', user_detail_update, name='user_detail_update_url'),
    path('<str:username>/delete/', UserDelete.as_view(), name='user_detail_delete_url'),
]