from django.urls import path
from apps.historiaMedica.views import ListadoHistoriaMedica

urlpatterns = [
    path('listado/', 
        ListadoHistoriaMedica.as_view(
            template_name = 'historia_medica_listar.html',
            extra_context = {'titulo': 'Listado General', 'title':'Historias Médicas'},
        ), 
        name='listar-historia'),
]