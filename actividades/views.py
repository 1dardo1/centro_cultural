from django.shortcuts import render, get_object_or_404, redirect
from .models import Actividad
from .forms import ActividadForm
from .models import UsuarioInscrito
from .forms import UsuarioForm
from .models import Sala
from .forms import SalaForm
from .models import Monitor
from .forms import MonitorForm
from .models import ResponsableSala
from .forms import ResponsableSalaForm

# Actividades
def lista_actividades(request):
    actividades = Actividad.objects.all()
    tipo = request.GET.get('tipo')
    monitor = request.GET.get('monitor')

    if tipo:
        actividades = actividades.filter(tipo__iexact=tipo)
    if monitor:
        actividades = actividades.filter(monitor__nombre__icontains=monitor)
    return render(request, 'actividades/lista_actividades.html', {'actividades': actividades})

def detalle_actividad(request, id):
    actividad = get_object_or_404(Actividad, id=id)
    return render(request, 'actividades/detalle_actividad.html', {'actividad': actividad})

def crear_actividad(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_actividades')
    else:
        form = ActividadForm()
    return render(request, 'actividades/form_actividad.html', {'form': form})

def editar_actividad(request, id):
    actividad = get_object_or_404(Actividad, id=id)
    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('detalle_actividad', id=id)
    else:
        form = ActividadForm(instance=actividad)
    return render(request, 'actividades/form_actividad.html', {'form': form})

def eliminar_actividad(request, id):
    actividad = get_object_or_404(Actividad, id=id)
    if request.method == 'POST':
        actividad.delete()
        return redirect('lista_actividades')
    return render(request, 'actividades/eliminar_confirmacion.html', {'actividad': actividad})

def listar_inscripciones(request, id):
    actividad = get_object_or_404(Actividad, id=id)
    usuarios = actividad.usuarios.all()
    return render(request, 'actividades/lista_inscripciones.html', {'actividad': actividad, 'usuarios': usuarios})

def inscribir_usuario(request, id):
    actividad = get_object_or_404(Actividad, id=id)
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        usuario = get_object_or_404(UsuarioInscrito, id=usuario_id)
        actividad.usuarios.add(usuario)
        return redirect('listar_inscripciones', id=id)
    usuarios = UsuarioInscrito.objects.exclude(id__in=actividad.usuarios.all())
    return render(request, 'actividades/inscribir_usuario.html', {'actividad': actividad, 'usuarios': usuarios})

def eliminar_inscripcion(request, id, usuario_id):
    actividad = get_object_or_404(Actividad, id=id)
    usuario = get_object_or_404(UsuarioInscrito, id=usuario_id)
    if request.method == 'POST':
        actividad.usuarios.remove(usuario)
        return redirect('listar_inscripciones', id=id)
    return render(request, 'actividades/eliminar_inscripcion.html', {'actividad': actividad, 'usuario': usuario})


#Usuario

def lista_usuarios(request):
    actividad_id = request.GET.get('actividad')
    usuarios = UsuarioInscrito.objects.all()
    if actividad_id:
        usuarios = usuarios.filter(actividad__id=actividad_id)
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/form_usuario.html', {'form': form})

def detalle_usuario(request, id):
    usuario = get_object_or_404(UsuarioInscrito, id=id)
    return render(request, 'usuarios/detalle_usuario.html', {'usuario': usuario})

def editar_usuario(request, id):
    usuario = get_object_or_404(UsuarioInscrito, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('detalle_usuario', id=id)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/form_usuario.html', {'form': form})

def eliminar_usuario(request, id):
    usuario = get_object_or_404(UsuarioInscrito, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'usuarios/eliminar_confirmacion.html', {'usuario': usuario})

def usuarios_por_actividad(request):
    actividad_id = request.GET.get('actividad')
    usuarios = []

    if actividad_id:
        actividad = get_object_or_404(Actividad, pk=actividad_id)
        usuarios = actividad.usuarios.all()

    return render(request, 'usuarios/por_actividad.html', {
        'usuarios': usuarios,
        'actividad_id': actividad_id
    })

# Monitores

def lista_monitores(request):
    monitores = Monitor.objects.all()
    return render(request, 'monitores/lista_monitores.html', {'monitores': monitores})

def crear_monitor(request):
    if request.method == 'POST':
        form = MonitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_monitores')
    else:
        form = MonitorForm()
    return render(request, 'monitores/form_monitor.html', {'form': form})

def detalle_monitor(request, id):
    monitor = get_object_or_404(Monitor, id=id)
    return render(request, 'monitores/detalle_monitor.html', {'monitor': monitor})

def editar_monitor(request, id):
    monitor = get_object_or_404(Monitor, id=id)
    if request.method == 'POST':
        form = MonitorForm(request.POST, instance=monitor)
        if form.is_valid():
            form.save()
            return redirect('detalle_monitor', id=id)
    else:
        form = MonitorForm(instance=monitor)
    return render(request, 'monitores/form_monitor.html', {'form': form})

def eliminar_monitor(request, id):
    monitor = get_object_or_404(Monitor, id=id)
    if request.method == 'POST':
        monitor.delete()
        return redirect('lista_monitores')
    return render(request, 'monitores/eliminar_confirmacion.html', {'monitor': monitor})

##Salas
def lista_salas(request):
    salas = Sala.objects.all()
    return render(request, 'salas/lista_salas.html', {'salas': salas})

def crear_sala(request):
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_salas')
    else:
        form = SalaForm()
    return render(request, 'salas/form_sala.html', {'form': form})

def detalle_sala(request, id):
    sala = get_object_or_404(Sala, id=id)
    return render(request, 'salas/detalle_sala.html', {'sala': sala})

def editar_sala(request, id):
    sala = get_object_or_404(Sala, id=id)
    if request.method == 'POST':
        form = SalaForm(request.POST, instance=sala)
        if form.is_valid():
            form.save()
            return redirect('detalle_sala', id=id)
    else:
        form = SalaForm(instance=sala)
    return render(request, 'salas/form_sala.html', {'form': form})

def eliminar_sala(request, id):
    sala = get_object_or_404(Sala, id=id)
    if request.method == 'POST':
        sala.delete()
        return redirect('lista_salas')
    return render(request, 'salas/eliminar_confirmacion.html', {'sala': sala})

#Responsables

def lista_responsables(request):
    responsables = ResponsableSala.objects.all()
    return render(request, 'responsables/lista_responsables.html', {'responsables': responsables})

def crear_responsable(request):
    if request.method == 'POST':
        form = ResponsableSalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_responsables')
    else:
        form = ResponsableSalaForm()
    return render(request, 'responsables/form_responsable.html', {'form': form})

def detalle_responsable(request, id):
    responsable = get_object_or_404(ResponsableSala, id=id)
    return render(request, 'responsables/detalle_responsable.html', {'responsable': responsable})

def editar_responsable(request, id):
    responsable = get_object_or_404(ResponsableSala, id=id)
    if request.method == 'POST':
        form = ResponsableSalaForm(request.POST, instance=responsable)
        if form.is_valid():
            form.save()
            return redirect('detalle_responsable', id=id)
    else:
        form = ResponsableSalaForm(instance=responsable)
    return render(request, 'responsables/form_responsable.html', {'form': form})

def eliminar_responsable(request, id):
    responsable = get_object_or_404(ResponsableSala, id=id)
    if request.method == 'POST':
        responsable.delete()
        return redirect('lista_responsables')
    return render(request, 'responsables/eliminar_confirmacion.html', {'responsable': responsable})

