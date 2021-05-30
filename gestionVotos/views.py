from django.shortcuts import render
from django.http import HttpResponse, request
from gestionVotos.models import Acta
from django.db.models import Count, Sum
from django.core.mail import send_mail
from django.conf import settings
from gestionVotos.forms import FormularioContacto

# Create your views here.
def busquedas_actas(request):
    return render(request,"busquedasActas.html")
def buscar(resquest):

    if resquest.GET["acta"]:
    
        #mensaje= "Articulo Buscados %r" %resquest.GET["acta"]
        acta= resquest.GET["acta"]
        if len(acta) > 20:
            mensaje="texto de busqueda demasiado largo"
        else:
            actas= Acta.objects.filter(tipo_casilla__icontains=acta)
            total_cheloCano= Acta.objects.aggregate(total= Sum('num_votoChelo'))
            total_morena= Acta.objects.aggregate(total= Sum('num_votoMorena')) 
           

            
            #es como si usara el  like
            return render(resquest, "resultados_busquedas.html",{"acta1":total_cheloCano['total'],"query":acta} )
    else:
        mensaje= "no ha introducido nada "
    return HttpResponse(mensaje)
def contacto(request):
    if request.method=="POST":
        miFormlario= FormularioContacto(request.POST)
        if miFormlario.is_valid():
            intForm= miFormlario.cleaned_data
            send_mail(intForm['asunto'],intForm['mensaje'],
            intForm.get('email',''),['rmatico13@hotmal.com'])
            return render(request,"gracias.html")
    else:
        miFormlario= FormularioContacto()
    return render(request,"formulario_contacto.html",{"form":miFormlario})
    '''
        subject= request.POST["asunto"]
        message= request.POST["mensaje"] +" " + request.POST["email"]
        email_from= settings.EMAIL_HOST_USER
        recipient_list=["pcivilcunduacan@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
    return render(request,"contacto.html")
    '''
def resultados_votaciones(request):
    total_cheloCano= Acta.objects.aggregate(total= Sum('num_votoChelo'))
    total_morena= Acta.objects.aggregate(total= Sum('num_votoMorena')) 

    return render(request,"resultadosActas.html",{"resultado_cano":total_cheloCano['total'],"resultado_oscar":total_morena['total']})

#def totalvotos(request):
 #   return render()