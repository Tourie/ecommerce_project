from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from users.forms import RegistrationForm, UserAuthentificationForm


def main_page(request):
    return render(request, 'ecommerce/main_page.html', context={'clicked_main': 'active'})


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main_page_url')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'registration/registr.html', context)


def logout_view(request):
    logout(request)
    return redirect('main_page_url')


def login_view(request):
    context = {'invalid_login': False}
    if request.user.is_authenticated:
        return redirect('main_page_url')
    if request.POST:
        form = UserAuthentificationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('main_page_url')
            else:
                form = UserAuthentificationForm()
                context['invalid_login'] = True
    else:
        form = UserAuthentificationForm()
    context['login_form'] = form
    return render(request, 'registration/login.html', context)

