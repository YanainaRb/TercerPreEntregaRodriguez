# Create your views here.

from django.shortcuts import render, redirect
from .models import Servicio, Reserva, Perro
from .forms import ReservaForm, PerroForm
from django.http import HttpResponse


def lista_servicios(request):
    servicios = ["Lavado básico", "Lavado Premium", "Lavado Gold"]
    return render(request, 'AppCoderYanaina/lista_servicios.html', {'servicios': servicios})

def reservar_servicio(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            
            nombre_cliente = form.cleaned_data['nombre_cliente']
            celular = form.cleaned_data['celular']
            servicio_id = form.cleaned_data['servicio']
            fecha_reserva = form.cleaned_data['fecha_reserva']
            
            servicio = Servicio(
                nombre_cliente=nombre_cliente,
                celular=celular,
                servicio=servicio_id,
                fecha_reserva=fecha_reserva
            )
            servicio.save()
            
        return HttpResponse(f"""
        <p>Servicio: {servicio.nombre} reservado con éxito.</p>
    """)
    else:
        form = ReservaForm()
    return render(request, 'AppCoderYanaina/formulario_reserva.html', {'form': form})

def lista_perros(request):
    perros = Perro.objects.all()
    return render(request, 'AppCoderYanaina/lista_perros.html', {'perros': perros})

def agregar_perro(request):
    if request.method == 'POST':
        form = PerroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_perros')
    else:
        form = PerroForm()

    return render(request, 'AppCoderYanaina/agregar_perro.html', {'form': form})
   
