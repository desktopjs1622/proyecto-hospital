from django.urls import path
from apps.historiaMedica.views import ListadoHistoriaMedica, RegistroPaciente

app_name = 'historiaMedica'
urlpatterns = [
    path('listado/', 
        ListadoHistoriaMedica.as_view(
            template_name = 'historia_medica_listar.html',
            extra_context = {'titulo': 'Listado General', 'title':'Historias Médicas'},
        ), 
        name='listar-historia'),

    path('registro-de-paciente/',
        RegistroPaciente.as_view(
            template_name='registro_paciente_formulario.html',
            extra_context={'titulo': 'Registro', 'title': 'Registro de Paciente'},
        ), 
        name='registro-paciente'),
]