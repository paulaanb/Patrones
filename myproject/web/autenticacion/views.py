from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.utils.translation import activate



# Create your views here.

class VRegistro(View):
    def get(self,request):

        activate('es')

        form= UserCreationForm()

        return render(request,'registro/registro.html',{'form':form})

    def post(self,request):
        activate('es')

        form= UserCreationForm(request.POST)

        if form.is_valid():

            usuario=form.save()

            login(request,usuario)

            return redirect('home')
        
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            
            return render(request, 'registro/registro.html', {'form':form})
            

def cerrar_sesion(request):
    logout(request)
    messages.success(request,"Sesión cerrada exitosamente")
    return redirect('home')

def logear(request):
    activate('es')

    if request.method=='POST':
        form= AuthenticationForm(request, data=request.POST)
            
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get('username')
            contraseña=form.cleaned_data.get('password')
            usuario=authenticate(username=nombre_usuario,password=contraseña)
            if usuario is not None:
                login(request,usuario)
                return redirect('home')
            else:
                messages.error(request,"Los datos son incorrectos")

        else:
            messages.error(request,"Los datos son incorrectos")

    form= AuthenticationForm()
    return render(request,'login/login.html',{'form':form})
    