"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', main_page_view, name='main_page_url'),
    path('sign_up/', registration_view, name='registr_url'),
    path('logout/', logout_view, name='logout_url'),
    path('login/', login_view, name='login_url'),
    path('activate/<uidb64>/<token>', ActivateAccountView.as_view(), name='activate'),
    path('shops/', include('shops.urls')),
    path('secret_action/become_admin', secret_action),
    path('my_orders/', include('orders.urls')),
    path('<str:unknown_url>/', unknown_url_view)
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
