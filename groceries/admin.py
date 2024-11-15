from django.contrib import admin
from .models import Store, Product, Price, UserPreference

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'api_url', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'store', 'price', 'availability_date', 'location')

@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'preferred_location', 'max_price', 'categories')