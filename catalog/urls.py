from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ProductDetailView,
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    toggle_activity,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)
from catalog.views import contact

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="index"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "<int:pk>/product_update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "<int:pk>/product_delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path("contact/", contact, name="contact"),
    path("blog/", BlogListView.as_view(), name="blog"),
    path("<int:pk>/blog_detail/", BlogDetailView.as_view(), name="blog_detail"),
    path("blog_create/", BlogCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>/update", BlogUpdateView.as_view(), name="blog_update"),
    path("blog/<int:pk>/delete", BlogDeleteView.as_view(), name="blog_delete"),
    path("blog/<int:pk>/toggle_activity", toggle_activity, name="toggle_activity"),
]
