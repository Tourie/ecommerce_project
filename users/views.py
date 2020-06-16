from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *


def users_list(request):
    if request.user.is_authenticated:
        user = User.objects.all()
        return render(request, 'users/base_user_list.html', context={'users': user, 'clicked_users': 'active'})
    else:
        return redirect('login_url')


def user_detail_view(request, username):
    try:
        user = User.objects.get(username__iexact=username)
        return render(request, 'users/user_detail_page.html', context={'user': user})
    except User.DoesNotExist:
        return render(request, 'errors/error.html')


def user_detail_update(request, username):
    context = {}
    try:
        user = User.objects.get(username__iexact=username)
    except User.DoesNotExist:
        return render(request, 'errors/error.html')
    if user.username == request.user.username or request.user.is_superuser:
        if request.POST:
            form = UserUpdateForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('user_detail_update_url', form.clean_username())
        else:
            form = UserUpdateForm(
                initial={
                    "email": user.email,
                    "username": user.username,
                    "name": user.name,
                    "age": user.age
                }
            )
        context['user_updating_form'] = form
        return render(request, 'users/user_update_page.html', context)
    else:
        return render(request, 'errors/permission_error.html')


class UserDelete(View):
    def get(self, request, username):
        if not request.user.is_authenticated:
            return redirect('login_url')
        user = User.objects.get(username__iexact=username)
        if request.user.username == user.username or request.user.is_admin:
            if user:
                return render(request, 'users/user_delete_page.html', context={'user': user})
        else:
            return render(request, 'errors/permission_error.html')

    def post(self, request, username):
        user_find = User.objects.get(username__iexact=username)
        print(user_find.username)
        if user_find:
            user_find.delete()
            return redirect('main_page_url')
# Create your views here.
