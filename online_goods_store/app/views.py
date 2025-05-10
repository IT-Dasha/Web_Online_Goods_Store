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
    return render(request, 'catalog.html')
def product(request):
    return render(request, 'product.html')

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
        # product=Product()
        # product.productid = request.POST.get("productid")
        # product.price = request.POST.get("price")
        # product.stockquantity = request.POST.get("stockquantity")
        # # image = request.FILES['image']
        # product.fk_categoryid_id = request.POST.get('categoryid_id')
        # product.save()
        id_product=request.POST.get("productid")
        image = request.FILES['image']
        fs = FileSystemStorage()
        # save the image on MEDIA_ROOT folder
        file_name = fs.save(image.name, image)
        # get file url with respect to `MEDIA_URL`
        file_url = fs.url(file_name)
        return HttpResponse(file_url)
    categoryes = Category.objects.all()
    return render(request, 'change_product.html',{'categoryes': categoryes})


# Create your views here.
