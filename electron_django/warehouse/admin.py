from django.contrib import admin
from .models import Category, Item, ItemBySerial

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(ItemBySerial)
