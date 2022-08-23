from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.customer_home,name='picture'),
   path('about' ,views.customer_about,name='image')
   path('' ,views.customer_cart,name='cart')
   
]