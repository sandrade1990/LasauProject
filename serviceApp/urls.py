from django.contrib import admin
from django.urls import path
from serviceApp import views



urlpatterns = [

    path('servicios', views.servicios, name='Servicios'),
    
] 