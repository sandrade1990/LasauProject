from socket import fromshare
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from lubesApp.models import*

class UserRegisterForm( UserCreationForm):
    
    username = forms.CharField(label= 'Usuario')
    email = forms.EmailField()
    password1= forms.CharField(label= 'Contraseña', widget = forms.PasswordInput)
    password2= forms.CharField(label= 'Repetir contraseña', widget = forms.PasswordInput)
    
    first_name= forms.CharField(label='Nombre')
    last_name= forms.CharField(label='Apellido')
    
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2' ]

        help_texts= {k: '' for k in fields}
    
class UserEditForm(UserCreationForm):

    
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label= 'Modificar username')
    email= forms.EmailField(label='Modificar e-mail')
    password1= forms.CharField(label= 'Modificar contraseña', widget = forms.PasswordInput)
    password2= forms.CharField(label= 'Repetir contraseña', widget = forms.PasswordInput)

    first_name= forms.CharField(label='Modificar nombre')
    last_name= forms.CharField(label='Modificar apellido')

    class Meta:
        model =User
        fields =  fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

class Load(forms.Form):
    
    name=forms.CharField(max_length = 40)
    description = forms.CharField(max_length =100)
    initdate = forms.DateField()
    revisiondate = forms.DateField()
    status = forms.CharField(max_length = 40)
    file=forms.FileField()