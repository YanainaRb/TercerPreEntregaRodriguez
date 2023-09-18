from django import forms
from .models import Reserva, Perro

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre_cliente','celular']


class PerroForm(forms.ModelForm):
    class Meta:
        model = Perro
        fields = ['nombre', 'raza', 'edad', 'dueño']