from http.client import HTTPResponse
from tkinter import N
from django.shortcuts import render
from bibliotecaApp.models import Vehiculo
from django.db.models import Q 
from .forms import VehiculoLoad
from django.contrib import messages




def biblioteca(request): #busqyeda de objetos en la base.

    queryset = request.GET.get("buscar")
    biblioteca = Vehiculo.objects.all().order_by('Revision')
    
    if queryset:
        biblioteca = Vehiculo.objects.filter(
            Q(Nombre__icontains = queryset)|
            Q(Sector__icontains = queryset)
        ).distinct() 
        return render (request,"bibliotecaApp/biblioteca.html",{"vehiculos":biblioteca})
    else:
        biblioteca = Vehiculo.objects.all().order_by('Revision')

    return render (request,"bibliotecaApp/biblioteca.html",{"vehiculos":biblioteca})


def bibliotecaLoad(request): #busqueda de objetos en la base.

    if request.method =='POST':

        Nombre= request.POST['Nombre']

        if Vehiculo.objects.filter(Nombre = Nombre).exists():
            messages.error(request, "El nombre del procedimiento ya se encuentra registrado! eliga otro nombre.")
            return render (request,"bibliotecaApp/bibliotecaLoad.html")

        miFormulario = VehiculoLoad(request.POST, request.FILES)
        print(miFormulario)

        if miFormulario.is_valid():

            instance = miFormulario.cleaned_data
            Procedimiento =Vehiculo(
                Nombre =instance['Nombre'],
                Sector =instance['Sector'],
                Revision =instance['Revision'],
                Version=instance['Version'],
                Estado=instance['Estado'],
                File = instance['File'],
                Codigo = instance['Codigo']
                )
            Procedimiento.save()

            biblioteca = Vehiculo.objects.all().order_by('Revision')
            return render(request,"bibliotecaApp/biblioteca.html",{"vehiculos":biblioteca})
      
    else:

        miFormulario = VehiculoLoad()

    return render (request,"bibliotecaApp/bibliotecaLoad.html",{"miFormulario":miFormulario})


def eliminarProcedimiento(request, Procedimiento_Nombre):

    biblioteca = Vehiculo.objects.get(Nombre = Procedimiento_Nombre)
    biblioteca.delete()

    biblioteca = Vehiculo.objects.all().order_by('Revision')
    return render (request,"bibliotecaApp/biblioteca.html",{"vehiculos":biblioteca})


def modificarProcedimiento(request,Procedimiento_Nombre): #busqueda de objetos en la base.
    
    procedimiento = Vehiculo.objects.get(Nombre = Procedimiento_Nombre)
    print(Procedimiento_Nombre)
    
    if request.method =='POST':

        Nombre = request.POST['Nombre']

        if Vehiculo.objects.filter(Nombre = Nombre).exists():
            messages.error(request, "El nombre del procedimiento ya se encuentra registrado! eliga otro nombre.")
            return render (request,"bibliotecaApp/bibliotecaChange.html",{"Procedimiento_Nombre":Procedimiento_Nombre })

        form=VehiculoLoad(request.POST, request.FILES)
        print(form)
        
        if form.is_valid():

            instance = form.cleaned_data

            procedimiento.Nombre =instance['Nombre']
            procedimiento.Sector =instance['Sector']
            procedimiento.Revision =instance['Revision']
            procedimiento.Version=instance['Version']
            procedimiento.Estado=instance['Estado']
            procedimiento.File = instance['File']
            procedimiento.Codigo = instance['Codigo']
                
            procedimiento.save()

            procedimiento = Vehiculo.objects.all().order_by('Revision')
            return render(request,"bibliotecaApp/biblioteca.html",{"vehiculos":procedimiento})
      
    else:

            form = VehiculoLoad(initial={
                'Nombre':procedimiento.Nombre, 
                'Sector':procedimiento.Sector,
                'Revision': procedimiento.Revision,
                'Version':procedimiento.Version,
                'Estado':procedimiento.Estado,
                'File':procedimiento.File,
                'Codigo':procedimiento.Codigo})
            print(form)

    return render (request,"bibliotecaApp/bibliotecaChange.html",{"form":form,"Procedimiento_Nombre":Procedimiento_Nombre })
