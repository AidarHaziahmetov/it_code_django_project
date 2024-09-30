from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def shopping_cart(request):
    return HttpResponse("это страница корзины товаров")


def confirm_payment(request):
    return HttpResponse("это страница подверждения оплаты")


def tracking_order(request):
    return HttpResponse("это страница отслеживания заказа")
