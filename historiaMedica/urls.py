from django.urls import path

from historiaMedica.views import ListadoHistoriaMedica, RegistroHistoriaMedica

app_name = 'historiaMedica'
urlpatterns = [
    path(
        'listado_de_historia/', 
        ListadoHistoriaMedica.as_view(
            template_name = 'historia_medica_listar.html',
            extra_context = {'titulo': 'Listado General', 'title':'Historias Médicas'},
        ), 
        name='lista-historia'
    ),
    path(
        'registro_de_historia/',
        RegistroHistoriaMedica.as_view(
            template_name='historia_medica_formulario.html',
            extra_context={'titulo': 'Registro', 'title': 'Registro de Historia'},
        ), 
        name='registro-historia'
    ),
]