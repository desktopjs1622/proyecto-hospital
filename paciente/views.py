from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from configuraciones.models import Pais, Estado, Municipio, Ciudad, Parroquia
# Librerias de terceros
from dal import autocomplete

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
            queryset = queryset.filter(pais__icontains=self.q)
        return queryset


class EstadoAutoComplete(autocomplete.Select2QuerySetView):
    """AutoComplete para listar los estados asociados al pais
    de seleccion y tambien para poder filtarlos
    """

    def get_queryset(self):
        pais = self.forwarded.get('pais', None)

        queryset = Estado.objects.all()

        if pais:
            queryset = queryset.filter(pais_id=pais)
        
        if self.q:
            queryset = queryset.filter(estado__icontains=self.q)
        
        return queryset
        
class MunicipioAutoComplete(autocomplete.Select2QuerySetView):
    """AutoComplete para listar los municipios asociados
    a los estados
    """
    def get_queryset(self):
        estado = self.forwarded.get('estado', None)

        queryset = Municipio.objects.all()

        if estado:
            queryset = queryset.filter(estado_id=estado)
        
        if self.q:
            queryset = queryset.filter(municipio__icontains=self.q)
        
        return queryset

class CiudadAutoComplete(autocomplete.Select2QuerySetView):
    """AutoComplete para listar las ciudades pertenecientes
    a los municipios
    """
    def get_queryset(self):
        municipio = self.forwarded.get('municipio', None)

        queryset = Ciudad.objects.all()

        if municipio:
            queryset = queryset.filter(municipio_id=municipio)
        
        if self.q:
            queryset = queryset.filter(ciudad__icontains=self.q)
        
        return queryset

class ParroquiaAutoComplete(autocomplete.Select2QuerySetView):
    """AutoComplete para listar las parroquias pertenecientes
    a los municipios
    """

    def get_queryset(self):
        municipio = self.forwarded.get('municipio', None)

        queryset = Parroquia.objects.all()

        if municipio:
            queryset = queryset.filter(municipio_id=municipio)
        
        if self.q:
            queryset = queryset.filter(parroquia__icontains=self.q)
        
        return queryset


##############################################################################
'''Se Listara todos los pacientes registrados en el 
hospital
'''
class ListadoPaciente(TemplateView):
    pass


##############################################################################
'''clase para registrar nuevos pacientes en
edades comprendidas que tengan cedula de identidad
laminada los candidatos estan entre los 9 años hasta
los 110 años
'''
class RegistroPacienteView(SuccessMessageMixin, CreateView):

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto = super().get_context_data(**kwargs)
        contexto['form'] = self.object
        return contexto
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form(self.form_class)
        if (form.is_valid()):
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):

        self.object = form.save()
        return super().form_valid(form)

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(
            form=form))
