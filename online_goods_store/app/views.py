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


# Create your views here.
