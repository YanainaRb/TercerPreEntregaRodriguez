"""
URL configuration for ProyectoCoderRodriguezYanaina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppCoderYanaina.views import reservar_servicio, lista_servicios, lista_perros, agregar_perro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Reservar_servicio/', reservar_servicio, name='reservar_servicio'),
    path('ListaServicios/', lista_servicios, name='lista_servicios'),
    path('lista_perros/', lista_perros, name='lista_perros'),
    path('agregar_perro/', agregar_perro, name='agregar_perro'),  
]

