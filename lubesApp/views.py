
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from lubesApp.forms import Load 



def home(request):
    return render(request,"lubesApp/index.html")

def blog(request):
    return render (request,"lubesApp/blog.html")

def contacto(request):
    return render (request,"lubesApp/contacto.html")


