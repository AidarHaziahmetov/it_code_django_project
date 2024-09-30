from django.shortcuts import render  # noqa: F401
from django.http import HttpResponse
# Create your views here.


def product_catalog(request):
    return HttpResponse("это страница каталога товаров")


def search_product(request):
    return HttpResponse("это страница поиска товаров")


def product_information(request):
    return HttpResponse("это страница подробной информации о товаре")
