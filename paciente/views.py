from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect

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
    pass
