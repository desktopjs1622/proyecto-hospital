from django.shortcuts import render
from configuraciones.models import (
    SistemaAparatoBiologico, PatologiasGenerales)
# Librerias de terceros
from dal import autocomplete

##############################################################################
#########        Clase del autocomplete para sistemas               ##########
#########        biologicos y patologias o enfermedades             ##########
##############################################################################

class AparatoBiologicoAutoComplete(autocomplete.Select2QuerySetView):
    """AutoComplete para listar los sistemas o aparatos
    biologicos que se divide el cuerpo humano
    """
    def get_queryset(self):
        queryset = SistemaAparatoBiologico.objects.all()

        if self.q:
            queryset = queryset.filter(nombre_aparato__icontains=self.q)
        return queryset

class PatologiaAutoComplete(autocomplete.Select2QuerySetView):
    """Son las enfermedades quizas las mas comunes
    y son determinadas de acuerdo al aparato biologico
    y son aquellas que afectan la salud del cuerpo humano
    """

    def get_queryset(self):
        aparato_biologico = self.forwarded.get('aparato_biologico', None)

        queryset = PatologiasGenerales.objects.all()

        if aparato_biologico:
            queryset = queryset.filter(aparato_biologico_id=aparato_biologico)
        
        if self.q:
            queryset = queryset.filter(nombre_patologico__icontains=self.q)

        return queryset

    ##############################################################################
