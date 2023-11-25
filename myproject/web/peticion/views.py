from django.contrib import messages
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from carro.carro import Carro

from peticion.models import LineaPeticion, Peticion

from django.template.loader import render_to_string

from django.utils.html import strip_tags

from django.core.mail import send_mail

from .models import Combo

@login_required(login_url='/autenticacion/logear')
def procesar_peticion(request):
    peticion=Peticion.objects.create(user=request.user) 
    carro=Carro(request)  
    lineas_peticion=list() 
    for key, value in carro.carro.items(): 
        lineas_peticion.append(LineaPeticion(
            combo_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            peticion=peticion                
            ))

    LineaPeticion.objects.bulk_create(lineas_peticion) 
    enviar_mail(
        peticion=peticion,
        lineas_peticion=lineas_peticion,
        nombreusuario=request.user.username,
        email_usuario=request.user.email
        

    )

    messages.success(request, "El pedido se ha creado correctamente")
    
    return redirect('../menu')
    

def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/peticion.html", {
        "peticion": kwargs.get("peticion"),
        "lineas_peticion": kwargs.get("lineas_peticion"),
        "nombreusuario":kwargs.get("nombreusuario") 
                       
        })

    mensaje_texto=strip_tags(mensaje)
    from_email="pizzeriadelizioso@gmail.com"
    to="paulanb2000@gmail.com"
    send_mail(asunto,mensaje_texto,from_email,[to], html_message=mensaje)
    
