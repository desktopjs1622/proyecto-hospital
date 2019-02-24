from django.http import HttpResponse
from django.views.generic import TemplateView

'''Clase principal para listar todos los pacientes
que tienen su historia medica
'''
class ListadoHistoriaMedica(TemplateView):
    pass


'''clase para registrar nuevos pacientes en
edades comprendidas que tengan cedula de identidad
laminada los candidatos estan entre los 9 años hasta
los 110 años
'''
class RegistroPaciente(TemplateView):
    pass

