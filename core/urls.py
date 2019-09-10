from django.urls import path

from .views import (
    home, 
    checkout, 
    products,
)

# Create your views here.

app_name = 'core'

urlpatterns = [
    path('', home, name="home"),
    path('checkout/', checkout, name="checkout"),
    path('products/', products, name="products"),
]