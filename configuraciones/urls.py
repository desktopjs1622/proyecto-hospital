from django.urls import path
from configuraciones.views import (
    AparatoBiologicoAutoComplete, PatologiaAutoComplete)


app_name = 'configuracion'
urlpatterns = [
    path(
        'aparato-biologico/',
        AparatoBiologicoAutoComplete.as_view(),
        name='aparato-biologico'
    ),
    path(
        'patologias/',
        PatologiaAutoComplete.as_view(),
        name='patologias'
    ),
]