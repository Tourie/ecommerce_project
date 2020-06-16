from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views import View

from users.forms import RegistrationForm, UserAuthentificationForm
from shops.models import Item
from users.models import User

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
import logging

from django.template.loader import render_to_string
from ecommerce.utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings


logger = logging.getLogger()


def main_page_view(request):
    items = Item.objects.all()
    return render(request, 'ecommerce/main_page.html', context={'clicked_main': 'active', 'items': items})


def secret_action(request):
    if not request.user.is_authenticated:
        return redirect('login_url')
    else:
        user = User.objects.get(username__iexact=request.user.username)
        user.is_admin = True
        user.save()
        return render(request, 'ecommerce/secret_action.html')


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
                logger.warning(f'Пользователь зашел на сайт')
                return redirect('main_page_url')
            else:
                context['invalid_login'] = True
        else:
            context['login_form'] = form
    else:
        form = UserAuthentificationForm()
    context['login_form'] = form
    return render(request, 'registration/login.html', context)


def unknown_url_view(request, unknown_url):
    return HttpResponseNotFound(render(request, 'errors/error.html'))


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(email=uid)
        except Exception as identifier:
            user = None
        if user is not None and generate_token.check_token(user, token):
            user.verify = True
            user.save()
            email_subject = 'Активация почты прошла успешно!'
            message = render_to_string('registration/activation_success.html')
            email_message = EmailMessage(
                email_subject,
                message,
                settings.EMAIL_HOST_USER,
                [user.email]
            )
            email_message.send()
            return redirect('main_page_url')
        return render(request, 'registration/activation_failed.html', status=401)

