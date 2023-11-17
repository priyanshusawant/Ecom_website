from django.shortcuts import render
from django.http import HttpResponse
from ecom.models import Item

# Create your views here.

def index(request):
    itemlist = Item.objects.all()

    context = {
        'itemlist':itemlist
    }

    return render(request, 'ecom/index.html', context)

def detail(request):
    return HttpResponse('<h1 style = "color : Orange">This is a details page</h1>')
