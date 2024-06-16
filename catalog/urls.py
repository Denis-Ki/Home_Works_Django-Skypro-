from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactView, BlogListView, BlogDetailView, BlogCreateView


app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="index"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("blog/", BlogListView.as_view(), name="blog"),
    path("blog_detail/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blog_create/", BlogCreateView.as_view(), name="blog_create"),

]