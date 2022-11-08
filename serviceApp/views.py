from django.shortcuts import render
from serviceApp.models import Servicio
# Create your views here.

def servicios(request):

    servicios=Servicio.objects.all()
    
    return render (request,"serviceApp/servicios.html",{"servicios":servicios})