from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from users.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.models import CusOrders

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                'Welcome {}, your account has been successfully created. Now you may login'.format(username)
            )
            form.save()
            return redirect('login')
        
    else:

        form = RegisterForm()
        
        context = {
            'form':form
        }

    return render(request, 'users/register.html', context)

def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.success(
                request,
                'Invalid Username or Password, Try again!'
            )
            return redirect('login')
        
        elif user.is_superuser:
            login(request, user)
            messages.success(
                request,
                'Welcome superuser {}, you have been successfully logged in'.format(request.user.username)
            )
            return redirect('ecom:index')

        if user is not None:
            login(request, user)
            messages.success(
                request,
                'Welcome {}, you have been successfully logged in'.format(request.user.username)
            )
            return redirect('ecom:index')
        
    
    return render(request, 'users/login.html')

def logout_view(request):
    messages.success(
        request,
        '{}, you have been successfully logged out'.format(request.user.username)
    )
    logout(request)
    return redirect('ecom:index')

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')


def orders(request, id, pdcd, user):

    context = {
        'pdcd':pdcd,
        'user':user
    }

    if request.method == 'POST':

        Obj_CusOrd = CusOrders(
            prod_code = pdcd,
            user = user,
            quantity = request.POSt.get('qty')
        )

        Obj_CusOrd.save()

        return redirect('ecom:detail', item_id = id)
    return render(request, 'users/orders.html', context)