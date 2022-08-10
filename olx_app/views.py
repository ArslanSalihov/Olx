from email.policy import default
from fileinput import filename
from itertools import product
from os import name
from tkinter import ALL
from tkinter.ttk import Entry
from turtle import title
from django.shortcuts import render,redirect,reverse
from .models import Product,Category,Favourite
from django.contrib.auth.models import User
from django.core.files.storage import  FileSystemStorage
from django.db.models import Q
from olx_app.forms import RegisterForm


def index(request):
    product = Product.objects.all()
    category = Category.objects.all()
    return render(request,'olx_app/index.html', {'product':product, 'category':category})

def c_product(request):
    product = Product.objects.all()
    category = Category.objects.all()
    return render(request,'olx_app/c_product.html', {'product':product, 'category':category})

def create(request):
    if request.method == 'POST':
        product = Product()
        product.title = request.POST.get('title')
        product.text = request.POST.get('text')
        product.price = request.POST.get('price')
        product.author = User.objects.get(id=request.user.id)
        category = Category.objects.all()
        if request.FILES.get('image',False) !=False:
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name,myfile)
            product.image = myfile
        product.save()
        return redirect('index')
    return render(request, 'olx_app', {'product':product, 'category':category})


def update(request,id):
    product = Product.objects.get(id = id)
    if request.method == 'POST':
        product.title = request.POST.get('title')
        product.text = request.POST.get('text')
        product.price = request.POST.get('price')
        if request.FILES.get('image',False) !=False:
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name,myfile)
            product.image = myfile
        product.author = User.objects.get(id=request.user.id)
        product.save()
        return redirect('index')
    return render(request, 'olx_app/update.html', {'product':product})

def delete_post(request,id):
    product = Product.objects.get(id = id)
    if request.method == 'POST':
        product.delete()
        return redirect(reverse('index'))
    return render(request, 'olx_app',{'product':product})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request,'olx_app/register.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request,'olx_app/registration/login.html', {'form':form})   

def product_detail(request,id):
    product = Product.objects.get(id = id)
    category = Category.objects.all()
    return render(request,'olx_app/product_detail.html', {'product':product , 'category':category})

def category_detail(request,id):
    category = Category.objects.get(id = id)
    product = Product.objects.all()
    return render(request, 'olx_app/category_detail.html',{'category':category , 'product':product})

def search(request):
    quary = request.GET.get('search')
    search_obj = Product.objects.filter(Q(title__icontains=quary))
    return render(request, 'olx_app/search.html', {'quary':quary, 'search_obj': search_obj})

def add_to_favourite(request,product_id):
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
        if not request.user.favourite_set.filter(product=product).exists():
            item = Favourite()
            item.product = product
            item.user = request.user
            item.save()
        return redirect('index')
    return redirect('authorisation')

def delete_favourite(request, product_id):
    item = Favourite.objects.get(id = product_id)
    if request.user.is_authenticated:
        item.delete()
        return redirect('favourite')
    return redirect('authorisation')

def favourite(request):
    if request.user.is_authenticated:
        product = Favourite.objects.filter(user=request.user)
        return render(request, 'olx_app/favourite.html', {'product':product})
    return redirect('authorisation')
