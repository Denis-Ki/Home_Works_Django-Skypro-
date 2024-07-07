from django.contrib import admin
from catalog.models import Product, Category, Blog, Version


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price_per_purchase", "category")
    list_filter = ("category",)
    search_fields = ("name", "description",)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "created_at")
    search_fields = ("title", "content",)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'number_version', 'name_version', 'is_activ_version')