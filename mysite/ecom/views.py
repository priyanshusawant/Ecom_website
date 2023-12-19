from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from ecom.models import Cart, Item, HISTORY
from ecom.forms import ItemForm
from ecom.models import HISTORY
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from users.models import CusOrders, CusRatingFeedback
from django.core.paginator import Paginator

# Create your views here.

def index(request):

    if request.user.is_superuser:
        itemlist = Item.objects.all()

        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains=item_name)

        # for pagination
        paginator = Paginator(itemlist, 3)
        page = request.GET.get('page')
        itemlist = paginator.get_page(page)

    elif request.user.is_authenticated and request.user.profile.user_type == 'Rest':
        itemlist = Item.objects.filter(for_user= request.user.username)

        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains=item_name)

    elif request.user.is_authenticated and request.user.profile.user_type == 'Cust':
        itemlist = Item.objects.all()

        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains=item_name)

    else:
        itemlist = Item.objects.all()

        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains=item_name)

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

    if request.user.profile.user_type == 'Rest' or request.user.profile.user_type == 'Admin':
        Obj_CusOrd = CusOrders.objects.filter(
            prod_code = item.prod_code
        )

    elif request.user.profile.user_type == 'Cust':
        Obj_CusOrd = CusOrders.objects.filter(
            prod_code = item.prod_code,
            user = request.user.username
        )

        crf = CusRatingFeedback.objects.filter(
            prod_code = item.prod_code
        )

    context = {
        'item':item,
        'hist':hist,
        'oco':Obj_CusOrd,
        'crf':crf
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
        Obj_History = HISTORY(
            user_name = self.request.user.username,
            prod_ref = form.instance.prod_code,
            item_name = self.request.POST.get('item_name'), 
            op_type = 'Created'
        )
        print(1)
        Obj_History.save()
        return super().form_valid(form)

#Category view

def category(request, val):

    if request.user.is_superuser:
        itemlist = Item.objects.all()

    elif request.user.is_authenticated and request.user.profile.user_type == 'Rest':
        itemlist = Item.objects.filter(for_user= request.user.username)

    elif request.user.is_authenticated and request.user.profile.user_type == 'Cust':
        itemlist = Item.objects.all()

    else:
        itemlist = Item.objects.all()

    print(val)
    items = Item.objects.filter(
        category = val
    )
    
    context = {
        'items' : items,
        'itemlist': itemlist
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

        Obj_History = HISTORY(
            user_name = request.user.username,
            prod_ref = item.prod_code,
            item_name = item.item_name,
            op_type = 'Deleted'
        )

        Obj_History.save()

        item.delete()
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

def NavForm(request):

    path = request.GET.get('item_name')
    nfd = request.GET.get('navformdata')
    print(nfd)

    return redirect(str(path))