from django.shortcuts import render
from .models import Item

# Create your views here.

def get_items_list(request):
    results = Item.objects.all()
    return render(request, "warehouse/items_list.html", {'items': results, 'title': 'Warehouse items'})
