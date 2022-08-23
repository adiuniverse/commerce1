from django.shortcuts import render

# Create your views here.
def customer_home(request):
    return render(request,'customer/home.html')
def customer_about(request):
    return render(request,'customer/about.html')
def customer_cart(request):
    return render(request,'customer/cart.html')












