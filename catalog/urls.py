from django.urls import path
from catalog.views import product_catalog, search_product, product_information

urlpatterns = [
    path("catalog/", product_catalog),
    path("search_product/", search_product),
    path("product_information/", product_information),
]
