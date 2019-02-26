from django.urls import path
from paciente.views import ListadoPaciente, RegistroPaciente

app_name = 'paciente'
urlpatterns = [
    path( #listar
        'listado_de_paciente/', 
        ListadoPaciente.as_view(
            template_name = 'paciente_listar.html',
            extra_context = {'titulo': 'Listado General', 'title':'Historias Médicas'},
        ), 
        name='lista-paciente'
    ),
    path(#agregar
        'registro-de-paciente/',
        RegistroPaciente.as_view(
            template_name='paciente_formulario.html',
            extra_context={'titulo': 'Registro', 'title': 'Registro de Paciente'},
        ), 
        name='registro-paciente'
    ),
]
