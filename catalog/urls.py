from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import product_list
from catalog.views import contact

app_name = CatalogConfig.name

urlpatterns = [
    path("", product_list, name="index"),
    path("contact/", contact, name="contact")
]