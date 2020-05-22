from django.shortcuts import render
from .models import *


def users_list(request):
    names = ['Makar', 'Nastya', 'Zhanna', 'Vladimir']
    return render(request, 'users/base_user_card.html', context={'names': names, 'clicked_users': 'active'})


def user_detail(request, username):
    return render(request, 'users/user_detail_page.html', context={'user': user})
# Create your views here.
