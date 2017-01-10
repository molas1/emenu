from django.contrib import admin

from .models import Menu, Dish


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'modified')
    search_fields = ('id', 'name')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'menu', 'price', 'vegan', 'created', 'modified')
    search_fields = ('id', 'name', 'menu__name')
