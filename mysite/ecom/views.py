from django.shortcuts import render
from django.http import HttpResponse
from ecom.models import Item
from ecom.models import HISTORY

# Create your views here.

def index(request):
    itemlist = Item.objects.all()

    context = {
        'itemlist':itemlist
    }

    return render(request, 'ecom/home.html', context)

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
