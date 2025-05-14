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


    # Usuarios
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/nuevo/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/<int:id>/', views.detalle_usuario, name='detalle_usuario'),
    path('usuarios/<int:id>/editar/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/<int:id>/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),
    path('usuarios_por_actividad/', views.usuarios_por_actividad, name='usuarios_por_actividad'),

    # Monitores
    path('monitores/', views.lista_monitores, name='lista_monitores'),
    path('monitores/nuevo/', views.crear_monitor, name='crear_monitor'),
    path('monitores/<int:id>/', views.detalle_monitor, name='detalle_monitor'),
    path('monitores/<int:id>/editar/', views.editar_monitor, name='editar_monitor'),
    path('monitores/<int:id>/eliminar/', views.eliminar_monitor, name='eliminar_monitor'),

    # Salas
    path('salas/', views.lista_salas, name='lista_salas'),
    path('salas/nueva/', views.crear_sala, name='crear_sala'),
    path('salas/<int:id>/', views.detalle_sala, name='detalle_sala'),
    path('salas/<int:id>/editar/', views.editar_sala, name='editar_sala'),
    path('salas/<int:id>/eliminar/', views.eliminar_sala, name='eliminar_sala'),

    # Responsable
    path('responsables/', views.lista_responsables, name='lista_responsables'),
    path('responsables/nuevo/', views.crear_responsable, name='crear_responsable'),
    path('responsables/<int:id>/', views.detalle_responsable, name='detalle_responsable'),
    path('responsables/<int:id>/editar/', views.editar_responsable, name='editar_responsable'),
    path('responsables/<int:id>/eliminar/', views.eliminar_responsable, name='eliminar_responsable'),

]
