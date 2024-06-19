from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ClienteForm
from .models import Cliente

# Create your views here.

def index(request):
    return render(request, 'otb/index.html')

def registro(request):
    if request.method == 'GET':
        return render(request, 'otb/registro.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'otb/registro.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'otb/registro.html', {
                    'form': UserCreationForm,
                    'error': 'Las Contraseñas no coinciden'
                })
    

def cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            rut = form.cleaned_data['rut']
            nombre = form.cleaned_data['nombre']
            aPaterno = form.cleaned_data['aPaterno']
            aMaterno = form.cleaned_data['aMaterno']
            fono = form.cleaned_data['fono']
            edad = form.cleaned_data['edad']
            deposito = form.cleaned_data['deposito']
            email = form.cleaned_data['email']
            # cliente = authenticate(rut=rut, nombre=nombre, aPaterno=aPaterno, aMaterno=aMaterno, fono=fono, edad=edad, deposito=deposito, email=email)
            cliente.save(rut=rut, nombre=nombre, aPaterno=aPaterno, aMaterno=aMaterno, fono=fono, edad=edad, deposito=deposito, email=email)
            return render(request, 'otb/index.html')
        else:
            context = {'form':ClienteForm, 'msj':'Error, intente de nuevo...'}
            return render(request, 'otb/cliente.html', context)
        
    return render(request, 'otb/cliente.html', {'form':ClienteForm})






# def registro(request):
#     if request.method == 'POST':
#       form = UserCreationForm(request.POST)
#       if form.is_valid():
#          form.save()
#          n_usuario = form.cleaned_data['n_usuario']
#          contrasena = form.cleaned_data['contrasena1']
#          usuario = authenticate(n_usuario=n_usuario, contrasena=contrasena)
#          login(request, n_usuario)
#          messages.success(request, ("Registro exitoso!"))
#          return redirect('otb/login.html')
#       else:
#          print(form.errors)
#     else:
#         form=UserCreationForm()
    
#     return render(request, 'otb/registro.html', {'form':form,})

def signin(request):
    if request.method == 'GET':
        return render(request, 'otb/login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'otb/login.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('index')
        
def signout(request):
    logout(request)
    return redirect('index')

def reserva(request):
    cliente=Cliente.objects.raw('SELECT * FROM otb_cliente')
    context={"cliente":cliente}
    return render(request, 'otb/reserva.html', context)




# def reserva(request):
#     cliente=Cliente.objects.raw('SELECT * FROM otb_cliente')
#     context={"cliente":cliente}
#     return render(request, 'otb/reserva.html', context)

# def cliente(request):
#     if request.method == 'GET':
#         return render(request, 'otb/cliente.html', {
#             'form': ClienteForm()
#         })
#     else:
#         Cliente.objects.create(rut=request.POST['rut'],
#                                nombre=request.POST['nombre'],
#                                aPaterno=request.POST['aPaterno'],
#                                aMaterno=request.POST['aMaterno'],
#                                fono=request.POST['fono'],
#                                edad=request.POST['edad'],
#                                deposito=request.POST['deposito'],
#                                email=request.POST['email'])
#         return render(request, 'otb/cliente.html', {
#             'form': ClienteForm()
#         })

# def cliente(request):
#     if request.method == "POST":
#         form = ClienteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             rut = request.POST['rut']
#             nombre = request.POST['nombre']
#             aPaterno = request.POST['aPaterno']
#             aPaterno = request.POST['aMaterno']
#             edad = request.POST['edad']
#             deposito = request.POST['deposito']
#             fono = request.POST['fono']
#             email = request.POST['email']
            
            
#             cliente = Cliente.objects.create(
#             rut=rut,
#             nombre=nombre,
#             apellido_paterno=aPaterno,
#             apellido_materno=aPaterno,
#             edad=edad,
#             deposito=deposito,
#             fono=fono,
#             email=email
#             )
#             cliente.save()            
#             messages.success(request, ("Registro exitoso!"))
#             return render(request, 'otb/cliente.html')            
#         else:
#             print(form.errors)           
#     else:
#         messages.error(request, ("Ocurrio un error, intente de nuevo..."))
#         return render(request, 'otb/cliente.html')
    

# def cliente(request):
#     if request.method == 'GET':
#         return render(request, 'cliente.html', {
#             'form': UserCreationForm
#         })
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             #register user
#             try:
#                 user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
#                 user.save()
#                 return render(request, 'cliente.html', {
#                     'form': UserCreationForm
#                 })
            
#             except IntegrityError:
#                 return render(request, 'cliente.html', {
#                     'form': UserCreationForm,
#                     'error': 'Usuario'
#                 })
#         return render(request, 'cliente.html', {
#                     'form': UserCreationForm,
#                     'error': 'Password do not match'
#                 })
    
    # def registro(request):
    # if request.method == 'POST':
    #   form = UserCreationForm(request.POST)
    #   if form.is_valid():
    #      form.save()
    #      n_usuario = form.cleaned_data['n_usuario']
    #      contrasena = form.cleaned_data['contrasena1']
    #      usuario = authenticate(n_usuario=n_usuario, contrasena=contrasena)
    #      login(request, usuario)
    #      messages.success(request, ('Registro exitoso!'))
    #      return redirect('otb/login.html')
    #   else:
    #      print(form.errors)
    # else:
    #     form=UserCreationForm()