from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category, Customer, Order, Purchase, Report
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.conf import settings


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

def add_product(request):
    if 'save' in request.POST:
        productid = request.POST.get('productid')
        price = request.POST.get('price')
        stockQuantity = request.POST.get('stockQuantity')
        image = request.FILES['image']
        fk_categoryid = request.POST.get('fk_categoryid')
        product=Product()
        product.save(force_insert=True)
        max_pk = productid
        for image in request.FILES.getlist('image'):
                    import requests
                    directory =  max_pk
                    parent_dir = f"{settings.MEDIA_ROOT}"
                    path = os.path.join(parent_dir, directory) 
        return HttpResponseRedirect (reverse('catalog'))
    Category = Category.objects.all()
    return render(request, 'change_product.html',{'Category': Category})


# Create your views here.
