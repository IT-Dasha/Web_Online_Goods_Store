from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category, Customer, Order, Purchase, Report
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request, 'home.html')

def catalog(request):
    products = Product.objects.all()
    categoryes = Category.objects.all()
    if request.POST:
        category_id=request.POST.get('categoryid_id')
        search=request.POST.get('search')
        if category_id=='' and search=='':
            products = Product.objects.all()
        elif category_id !='' and search !='':
             products = Product.objects.filter(fk_categoryid=category_id,  price=search)
        elif category_id =='' and search !='':
            products = Product.objects.filter(price=search)
        else:
            products = Product.objects.all()
        products = products.filter(fk_categoryid=category_id) 
        return render(request, 'catalog.html', {'products': products, 'categoryes': categoryes})
    return render(request, 'catalog.html', {'products': products, 'categoryes': categoryes})
def product(request, product_id):
    products = Product.objects.filter(productid=product_id).select_related('fk_categoryid')
    return render(request, 'product.html',context={'products': products})

def order_placing(request):
    return render(request, 'order_placing.html')

def authorization(request):
    return render(request, 'authorization.html')

def registration(request):
    return render(request, 'registration.html')

def output_password(request):
    return render(request, 'output_password.html')

def reporting(request):
     data = {
        'labels': ['Январь', 'Февраль', 'Март', 'Апрель', 'Май'],
        'data': [12, 19, 3, 5, 2]
    }
     return render(request, 'reporting.html', {'data': data})

def personal_account(request):
    return render(request, 'personal_account.html')

def change_product(request):
    return render(request, 'personal_account.html')

def add_product(request):
    if 'save' in request.POST:
        product=Product()
        product.productid = request.POST.get("productid")
        product.price = request.POST.get("price")
        product.stockquantity = request.POST.get("stockquantity")
        product.fk_categoryid_id = request.POST.get('categoryid_id')
        product.save()
        id_product=request.POST.get("productid")
        image = request.FILES['image']
        fs = FileSystemStorage()
        # save the image on MEDIA_ROOT folder
        file_name = fs.save(id_product+".png", image)
        # get file url with respect to `MEDIA_URL`
        file_url = fs.url(file_name)
        return HttpResponseRedirect (reverse ('catalog'))
    categoryes = Category.objects.all()
    return render(request, 'change_product.html',{'categoryes': categoryes})
from django.core.files.storage import FileSystemStorage
def qwe(request):
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage() #defaults to   MEDIA_ROOT  
        filename = fs.save(myfile.name, myfile)
        file_url = fs.url(filename)
        
        return HttpResponse(f"Image saved at: {file_url}")

    return render(request, 'qwe.html')

# Create your views here.
