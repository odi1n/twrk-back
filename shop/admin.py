from django.contrib import admin

from shop.models import Product, Category, PropertyObject, PropertyValue


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }
    list_display = ("title", "sku", "slug", "category",)
    list_filter = ('status',)


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }
    list_display = ('title', 'slug')


@admin.register(PropertyObject)
class PropertyObjectModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'code': ['title']
    }
    list_display = ('title', 'code', 'value_type',)


@admin.register(PropertyValue)
class PropertyValueModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'code': ['value_string', 'value_decimal']
    }
    list_display = ('property_object', 'value_string', 'value_decimal', 'code',)
