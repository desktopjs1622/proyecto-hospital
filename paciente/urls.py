from django.urls import path
from django.views.generic import TemplateView
from paciente.views import (
    ListadoPaciente, RegistroPaciente, PaisAutoComplete, EstadoAutoComplete,
    MunicipioAutoComplete, CiudadAutoComplete, ParroquiaAutoComplete)

app_name = 'paciente'
urlpatterns = [
    # #################### Servicios de auto completado #################### #
    path(
        'pais/', 
        PaisAutoComplete.as_view(), 
        name='pais'
    ),
    path(
        'estado/',
        EstadoAutoComplete.as_view(),
        name='estado'
    ),
    path(
        'municipio/',
        MunicipioAutoComplete.as_view(),
        name='municipio'
    ),
    path(
        'ciudad/',
        CiudadAutoComplete.as_view(),
        name='ciudad'
    ),
    path(
        'parroquia/',
        ParroquiaAutoComplete.as_view(),
        name='parroquia'
    ),
    # ################ rutas para los template paciente #################### #
    path( #listar
        'listado/', 
        ListadoPaciente.as_view(
            template_name = 'paciente_listar.html',
            extra_context = {'titulo': 'Listado General', 'title':'Historias Médicas'},
        ), 
        name='lista-paciente'
    ),
    path( #Detalle
        'listado/detalle', 
        TemplateView.as_view(
            template_name='paciente_detalle.html',
            extra_context = {'titulo': 'Paciente'}
        ), 
        name='detalle-paciente'
    ),
    path( #Eliminar
        'listado/eliminar', 
        TemplateView.as_view(
            template_name='paciente_eliminar.html',
            extra_context = {'titulo': 'Paciente'}
        ), 
        name='eliminar-paciente'
    ),
    path( #agregar
        'registro/agregar',
        RegistroPaciente.as_view(
            template_name='paciente_formulario.html',
            extra_context={'titulo': 'Registro', 'title': 'Registro de Paciente'},
        ), 
        name='registro-paciente'
    ),
    path( #agregar
        'registro/editar',
        RegistroPaciente.as_view(
            template_name='paciente_formulario.html',
            extra_context={'titulo': 'Registro', 'title': 'Registro de Paciente'},
        ), 
        name='editar-paciente'
    ),
    
]
