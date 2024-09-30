from django.urls import path
from login_app.views import login, register, recovery_password

urlpatterns = [
    path("login/", login),
    path("register/", register),
    path("recovery_password/", recovery_password),
]
