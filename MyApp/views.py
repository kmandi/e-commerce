from django.shortcuts import render
from django.views import View

from .models import Cart, Customer, OrderPlaced, Product


# Create your views here.
class ProductView(View):
 def get(self, request):
  topwears = Product.objects.filter(category='TW')
  bottomwears = Product.objects.filter(category='BW')
  mobiles = Product.objects.filter(category='M')
  laptops = Product.objects.filter(category='L')
  return render(request, 'app/home.html', {'topwears': topwears, 'bottomwears': bottomwears, 'mobiles': mobiles, 'laptops': laptops})


# def product_detail(request):
#  return render(request, 'app/productdetail.html')
 
class ProductDetailView(View):
 def get(self, request, pk):
  product = Product.objects.get(pk=pk)
  return render(request, 'app/productdetail.html', {'product': product})
    

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

# mobile viewport
def mobile(request, data=None):
 if data == None:
  mobiles = Product.objects.filter(category='M')
 elif data == 'Motorola' or data == 'realme' or data == 'Samsung':
  mobiles = Product.objects.filter(category='M').filter(brand=data)
 elif data == 'below':
  mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=10000)
 elif data == 'above':
  mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=10000)
 return render(request, 'app/mobile.html', {'mobiles': mobiles})

# Laptop viewport
def laptop(request, data=None):
 if data == None:
  laptops = Product.objects.filter(category='L')
 elif data == 'HP' or data == 'ASUS' or data == 'DELl' or data == 'Lenovo':
  laptops = Product.objects.filter(category='L').filter(brand=data)
 elif data == 'below':
  laptops = Product.objects.filter(category='L').filter(discounted_price__lt=60000)
 elif data == 'above':
  laptops = Product.objects.filter(category='L').filter(discounted_price__gt=60000)
 return render(request, 'app/laptop.html', {'laptops': laptops})


# Top Wear viewport
def topWear(request, data=None):
 if data == None:
  topWears = Product.objects.filter(category='TW')
 elif data == 'below':
  topWears = Product.objects.filter(category='TW').filter(discounted_price__lt=400)
 elif data == 'above':
  topWears = Product.objects.filter(category='TW').filter(discounted_price__gt=400)
 return render(request, 'app/topwear.html', {'topWears': topWears})


# Bottom Wear viewport
def bottomWears(request, data=None):
 if data == None:
  bottomWears = Product.objects.filter(category='BW')
 elif data == 'below':
  bottomWears = Product.objects.filter(category='BW').filter(discounted_price__lt=400)
 elif data == 'above':
  bottomWears = Product.objects.filter(category='BW').filter(discounted_price__gt=400)
 return render(request, 'app/bottomwear.html', {'bottomWears': bottomWears})


def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
