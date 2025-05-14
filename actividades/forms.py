from django import forms
from .models import Actividad, UsuarioInscrito, Monitor, Sala, ResponsableSala


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['nombre', 'tipo', 'horario', 'descripcion', 'duracion', 'plazas_disponibles', 'monitor', 'sala_principal']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = UsuarioInscrito
        fields = '__all__'

class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = ['nombre', 'especializacion']

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nombre', 'capacidad', 'ubicacion', 'responsable']



class ResponsableSalaForm(forms.ModelForm):
    class Meta:
        model = ResponsableSala
        fields = '__all__'
