from django.http import HttpResponse
from django.shortcuts import render


def main_page(request):
    return render(request, 'ecommerce/main_page.html', context={'clicked_main': 'active'})

