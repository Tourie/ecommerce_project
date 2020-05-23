from django.shortcuts import render, redirect
from .models import *


def users_list(request):
    if request.user.is_authenticated:
        user = User.objects.all()
        return render(request, 'users/base_user_list.html', context={'users': user, 'clicked_users': 'active'})
    else:
        return redirect('login_url')


def user_detail(request, username):
    try:
        user = User.objects.get(username__iexact=username)
        return render(request, 'users/user_detail_page.html', context={'user': user})
    except User.DoesNotExist:
        return render(request, 'ecommerce/../templates/errors/error.html')


def user_detail_update(request, username):
    user = User.objects.get(username__iexact=username)
    if user.username == request.user.username or request.user.is_superuser:
        pass
    else:
        return render(request, 'errors/permission_error.html')
# Create your views here.
