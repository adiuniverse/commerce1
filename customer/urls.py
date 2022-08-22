from django.urls import path
from . import views

urlpatterns = [
    path('home' ,views.customer_home,name='picture'),
   path('about' ,views.customer_about,name='image')
   
]