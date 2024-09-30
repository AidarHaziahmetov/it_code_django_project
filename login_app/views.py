from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def login(request):
    return HttpResponse("это страница входа")


def register(request):
    return HttpResponse("это страница регистрации")


def recovery_password(request):
    return HttpResponse("это страница востановления пароля")
