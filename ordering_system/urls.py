from django.urls import path
from ordering_system.views import shopping_cart, confirm_payment, tracking_order

urlpatterns = [
    path("card/", shopping_cart),
    path("payment/", confirm_payment),
    path("tracking_order/", tracking_order),
]
