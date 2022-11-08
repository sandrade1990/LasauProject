from django.contrib import admin
from django.urls import path
from bibliotecaApp import views


urlpatterns = [

    path('biblioteca', views.biblioteca, name='Biblioteca'), 
    path('bibliotecaLoad', views.bibliotecaLoad, name='BibliotecaLoad'),
    path('bibliotecaDelete/<Procedimiento_Nombre>', views.eliminarProcedimiento, name="BibliotecaDelete"),
    path('bibliotecaChange/<Procedimiento_Nombre>', views.modificarProcedimiento, name="BibliotecaChange"),
] 