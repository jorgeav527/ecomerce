from django.shortcuts import render

from .models import Item

# Create your views here.

def home(request):
    context = {
        "items": Item.objects.all(),   
    }
    return render(request, 'home-page.html', context)

def checkout(request):
    context = {
    }
    return render(request, 'checkout-page.html', context)

def products(request):
    context = {
    }
    return render(request, 'products-page.html', context)