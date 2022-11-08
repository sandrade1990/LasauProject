from django.contrib import admin
from django.urls import path
from lubesApp import views


urlpatterns = [

    path('', views.home, name='Home'),
    path('blog', views.blog, name='Blog'),
    path('contacto', views.contacto, name='Contacto'), 
    
] 

