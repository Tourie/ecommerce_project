import datetime
from multiprocessing import Process, Manager, Queue
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from ecommerce.utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
import logging
from .models import User

messages = Queue()
logger = logging.getLogger()


def send_verification(user,current_site):
    if user.verify:
        logger.warning('Попытка верифицировать подтвержденного пользователя!')
        return
    email_subject = 'Active your Account'
    message = render_to_string('registration/activate.html',
                               {
                                   'user': user,
                                   'domain': current_site.domain,
                                   'uid': urlsafe_base64_encode(force_bytes(user.email)),
                                   'token': generate_token.make_token(user),
                                   'date': datetime.date.today()
                               })
    email_message = EmailMessage(
        email_subject,
        message,
        settings.EMAIL_HOST_USER,
        [user.email]
    )
    logger.warning('Send mail')
    email_message.send()


def read_query_messages(request):
    while not messages.empty():
        user = messages.get()
        new_process = Process(target=send_verification, args=(user, get_current_site(request)))
        new_process.start()
        new_process.join()


def send_verifications(modeladmin, request, queryset):
    for user in list(queryset.all()):
        messages.put(user)
    p = Process(target=read_query_messages, args=(request,))
    p.start()
    p.join()


class UsersAdmin(UserAdmin):
    list_display = ('email', 'username', 'name', 'age', 'activity', 'date_joined', 'last_login')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    actions = [send_verifications]

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, UsersAdmin)
