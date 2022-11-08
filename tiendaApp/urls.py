from django.contrib import admin
from django.urls import path
from tiendaApp import views


urlpatterns = [

    path('tienda', views.tienda, name='Tienda'), 
    
] 