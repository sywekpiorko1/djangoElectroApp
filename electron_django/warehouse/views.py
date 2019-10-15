from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.

def get_items_list(request):
    results = Item.objects.all()
    return render(request, "warehouse/items_list.html", {'items': results, 'title': 'Warehouse items'})


def create_an_item(request):
    if request.method=="POST":

        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(get_items_list)
    
    else:

        form = ItemForm()

        return render(request, "warehouse/item_form.html", {'form': form, 'title': 'Add item'})