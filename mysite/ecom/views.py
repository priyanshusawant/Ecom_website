from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from ecom.models import Item
from ecom.models import HISTORY


# Create your views here.

def index(request):
    itemlist = Item.objects.all()

    context = {
        'itemlist':itemlist
    }

    return render(request, 'ecom/home.html', context)

# Detail view

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)

    hist = HISTORY.objects.filter(
        prod_ref = item.prod_code
    )

    context = {
        'item':item,
        'hist':hist
    }

    return render(request, "ecom/detail.html", context)

#Category view

def category(request, val):
    print(val)
    citem = Item.objects.filter(
        category = val
    )
    
    context = {
        'citem' : citem
    }
    
    return render(request, 'ecom/category.html', context)

#About us & Contact us

def about(request):
    return render(request, 'ecom/about.html')

def contact(request):
    return render(request, 'ecom/contact.html')

#Delete item view

def delete_item(request, id):
    item = Item.objects.get(pk=id)

    context = {
        'item':item
    }
    
    if request.method == 'POST':
        item.delete()

        Obj_History = HISTORY(
            user_name = request.user.username,
            prod_ref = item.prod_code,
            item_name = item.item_name,
            op_type = 'Deleted'
        )
        print(1)
        Obj_History.save()

        return redirect('ecom:index')

    return render(request, 'ecom/item-delete.html', context)

