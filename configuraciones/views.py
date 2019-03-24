from django.shortcuts import render
from configuraciones.models import (
    SistemaAparatoBiologico, PatologiasGenerales)
<<<<<<< HEAD
=======
from configuraciones.models import Pais, Estado, Municipio, Ciudad, Parroquia
>>>>>>> 0b1adcec9448a48e3d4d0d9a5009a2bfef56b9a1
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
#########           Clase del autocomplete de la División           ##########
#########                   politico territorial                    ##########
##############################################################################
class PaisAutoComplete(autocomplete.Select2QuerySetView):
    """AutoComplete para listar Pais
    """
    def get_queryset(self):
        queryset = Pais.objects.all()

        if self.q:
            queryset = queryset.filter(nombre_pais__icontains=self.q)
        return queryset


class EstadoAutoComplete(autocomplete.Select2QuerySetView):
    """AutoComplete para listar los estados asociados al pais
    de seleccion y tambien para poder filtarlos
    """

    def get_queryset(self):
        nombre_pais = self.forwarded.get('nombre_pais', None)

        queryset = Estado.objects.all()

        if nombre_pais:
            queryset = queryset.filter(nombre_pais_id=nombre_pais)
        
        if self.q:
            queryset = queryset.filter(nombre_estado__icontains=self.q)
        
        return queryset
        
class MunicipioAutoComplete(autocomplete.Select2QuerySetView):
    """AutoComplete para listar los municipios asociados
    a los estados
    """
    def get_queryset(self):
        nombre_estado = self.forwarded.get('nombre_estado', None)

        queryset = Municipio.objects.all()

        if nombre_estado:
            queryset = queryset.filter(nombre_estado_id=nombre_estado)
        
        if self.q:
            queryset = queryset.filter(nombre_municipio__icontains=self.q)
        
        return queryset

class CiudadAutoComplete(autocomplete.Select2QuerySetView):
    """AutoComplete para listar las ciudades pertenecientes
    a los municipios
    """
    def get_queryset(self):
        nombre_municipio = self.forwarded.get('nombre_municipio', None)

        queryset = Ciudad.objects.all()

        if nombre_municipio:
            queryset = queryset.filter(nombre_municipio_id=nombre_municipio)
        
        if self.q:
            queryset = queryset.filter(nombre_ciudad__icontains=self.q)
        
        return queryset

class ParroquiaAutoComplete(autocomplete.Select2QuerySetView):
    """AutoComplete para listar las parroquias pertenecientes
    a los municipios
    """

    def get_queryset(self):
        nombre_municipio = self.forwarded.get('nombre_municipio', None)

        queryset = Parroquia.objects.all()

        if nombre_municipio:
            queryset = queryset.filter(nombre_municipio_id=nombre_municipio)
        
        if self.q:
            queryset = queryset.filter(nombre_parroquia__icontains=self.q)
        
        return queryset

