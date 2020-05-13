from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Item
from .forms import ItemForm

# Create your views here.


def warehouse_items_list(request):
    results = Item.objects.all()
    if not results:
        messages.warning(request, f'No items in dbase, please add some logged as admin')
    template_name = "warehouse/items_list.html"
    context = {
        'items': results,
        'title': 'Warehouse items'
    }
    return render(request, template_name, context)


@staff_member_required(login_url='login')
def warehouse_create_view(request):
    
    if request.method == "POST":

        form = ItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
                        
            return redirect(warehouse_items_list)
    else:
        form = ItemForm()
        template_name = "warehouse/item_form.html"
        context = {
            'form': form,
            'title': 'Add new item to Warehouse'
        }
        return render(request, template_name, context)


def warehouse_detail_view(request, pk):
    # 1 object -> detail view
    item = get_object_or_404(Item, pk=pk)
    template_name = "warehouse/item_detail.html"
    context = {
        'item': item,
        'title': f"{item.name} details"
    }
    return render(request, template_name, context)


@staff_member_required
def warehouse_update_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    form = ItemForm(request.POST or None, request.FILES or None, instance=item)

    if request.method == 'POST':
        
        if form.is_valid():
            form.save()    

            messages.success(request, f"Item {item.name} updated in Warehouse")

            return redirect(reverse('warehouse-items-detail', kwargs={'pk': pk}))


    template_name = "warehouse/item_form.html"
    context = {
        'form': form,
        'title': f"Update {item.name} in Warehouse"
    }
    return render(request, template_name, context)


@staff_member_required
def warehouse_delete_view(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == "POST":
        item.delete()
        return redirect("/")

    template_name = "warehouse/item_delete.html"
    context = {
        "item": item
    }
    return render(request, template_name, context)
