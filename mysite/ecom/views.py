from django.shortcuts import render
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

