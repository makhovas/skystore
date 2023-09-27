from django.contrib import admin

from catalog.models import Category, Product, Contacts, Version


# admin.site.register(Category)


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)


# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('country', 'inn', 'address',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'is_active',)
