from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.contrib.auth import logout
from .models import Solicitud, TipoMaterial, puntitos
from datetime import datetime

def inicio(request):
    return render(request,'core/index.html')


def materiales(request):
    materiales = TipoMaterial.objects.all()
    data={
        "materiales": materiales
    }
    return render(request,'core/materiales.html',data)


def puntos(request):
    puntos = puntitos.objects.all()
    data={
        "puntos": puntos
    }
    return render(request,'core/puntos.html',data)


def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'],password=user_creation_form.cleaned_data['password1'])
            login(request,user)

            return redirect('inicio')
        
    return render(request,'registration/register.html',data)


def salir(request):
    logout(request)
    return redirect('inicio')


def solicitud(request,id=0):

    if(request.POST):

        tipomat = request.POST["txtMat"]
        cantidad = request.POST["txtCant"]
        fecha_str = request.POST["txtFecha"]
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()




        nuevaSol = Solicitud()
        nuevaSol.user = request.user  
        nuevaSol.tipomat= tipomat
        nuevaSol.cantidad = cantidad
        nuevaSol.fecha = fecha
        nuevaSol.save()
        return redirect('solicitud') 
    
    if id != 0:
        Solicitudes = Solicitud.objects.get(id=id)
        Solicitudes.delete()

    Solicitud_lista = Solicitud.objects.filter(user=request.user)

    data ={
        "solicitudes" : Solicitud_lista,
    }
    return render(request,'core/solicitud.html',data)

def metricas(request):
    soli_x_mes = (Solicitud.objects.annotate(mes=TruncMonth('fecha')).values('mes').annotate(total=Count('id')).order_by('mes'))
    tipomat_x_mes = (Solicitud.objects.values('tipomat').annotate(total=Count('id')).order_by('total'))

    data={
        'soli_x_mes': soli_x_mes,
        'tipomat_x_mes': tipomat_x_mes
    }

    return render(request,'core/metricas.html',data)


def recomendaciones(request):
    return render(request,'core/recomendaciones.html')
