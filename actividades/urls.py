from django.urls import path
from . import views

urlpatterns = [

    #Actividades
    path('', views.lista_actividades, name='lista_actividades'),
    path('actividades/', views.lista_actividades, name='lista_actividades'),
    path('actividades/nueva/', views.crear_actividad, name='crear_actividad'),
    path('actividades/<int:id>/', views.detalle_actividad, name='detalle_actividad'),
    path('actividades/<int:id>/editar/', views.editar_actividad, name='editar_actividad'),
    path('actividades/<int:id>/eliminar/', views.eliminar_actividad, name='eliminar_actividad'),
    path('actividades/<int:id>/inscripciones/', views.listar_inscripciones, name='listar_inscripciones'),
    path('actividades/<int:id>/inscribir/', views.inscribir_usuario, name='inscribir_usuario'),
    path('actividades/<int:id>/inscripciones/<int:usuario_id>/eliminar/', views.eliminar_inscripcion, name='eliminar_inscripcion'),
    ]