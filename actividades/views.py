from django.shortcuts import render, get_object_or_404, redirect
from .models import Actividad, UsuarioInscrito
from .forms import ActividadForm

# Create your views here.
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