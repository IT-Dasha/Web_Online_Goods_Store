from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

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
    return render(request, 'reporting.html')

def personal_account(request):
    return render(request, 'personal_account.html')

def change_product(request):
    return render(request, 'change_product.html')


# Create your views here.
