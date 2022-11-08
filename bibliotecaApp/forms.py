from django import forms
from django.forms.widgets import NumberInput

from bibliotecaApp.models import LasauPlanta

class VehiculoLoad(forms.Form):

    Nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre del Procedimiento', 'style': 'width: 500px;', 'class': 'form-control'}))
    Sector = forms.ModelChoiceField(queryset = LasauPlanta.objects.all(), initial=0, widget=forms.Select (attrs={'placeholder': 'Nombre del Procedimiento', 'style': 'width: 500px;', 'class': 'form-control'}))
    Revision= forms.DateField(widget=NumberInput(attrs={'type': 'date', 'style': 'width: 500px;', 'class': 'form-control'}))
    Version = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Versión del Procedimiento', 'style': 'width: 500px;', 'class': 'form-control'}))
    File = forms.FileField(required=True)
    Estado = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'placeholder': 'Estado', 'style': 'width: 500px;', 'class': 'form-control'}))
    Codigo = forms.CharField(max_length = 50,widget=forms.TextInput(attrs={'placeholder': 'Nombre Código', 'style': 'width: 500px;', 'class': 'form-control'}))

  
    