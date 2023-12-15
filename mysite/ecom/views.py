from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from ecom.models import Cart, Item
from ecom.forms import ItemForm
from ecom.models import HISTORY
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


# Create your views here.

def index(request):
    itemlist = Item.objects.all()

    context = {
        'itemlist':itemlist
    }

    return render(request, 'ecom/home.html', context)


class IndexClassView(ListView):

    model = Item
    context_object_name = 'itemlist'
    template_name = 'ecom/home.html'

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


class EcomDetail(DetailView):

    model = Item
    context_object_name = 'item'
    template_name = 'ecom/detail.html'

#Create Item Views
    

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('ecom:home')

    context = {
        'form':form
    }

    return render(request, 'ecom/item-form.html', context)



class CreateItem(CreateView):

    model = Item
    fields = ['prod_code', 'for_user', 'item_name', 'item_desc', 'item_price', 'item_img']
    template_name = 'ecom/item-form.html'
    success_url = reverse_lazy('ecom:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#Category view

def category(request, val):
    print(val)
    items = Item.objects.filter(
        category = val
    )
    
    context = {
        'items' : items
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

#Update Item View

def update_item(request, id):
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)

    context = {
        'form':form
    }

    if form.is_valid():
        form.save()

        Obj_History = HISTORY(
            user_name = request.user.username,
            prod_ref = form.instance.prod_code,
            item_name = request.POST.get('item_name'), #form.instance.item_name
            op_type = 'Updated'
        )
        print(1)
        Obj_History.save()

        return redirect('ecom:index')

    return render(request, 'ecom/item-form.html', context)

#Add-to-Cart

def add_to_cart(request):
    user = request.user_name
    prod_code = request.GET.get('prod_code')
    product = Item.objects.get(id=prod_code)
    Cart(user=user, product=Item).save()

    return redirect('/cart')

def show_cart(request):
    return render(request, 'ecom/addtocart.html')