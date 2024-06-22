from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cliente


class ClienteForm(forms.Form):
    rut = forms.CharField(max_length=10)
    nombre = forms.CharField(max_length=50)
    aPaterno = forms.CharField(max_length=50)
    aMaterno = forms.CharField(max_length=50)
    fono =  forms.IntegerField()
    edad = forms.IntegerField()
    deposito = forms.IntegerField()
    email = forms.EmailField()