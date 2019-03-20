from django import forms
from dal import autocomplete
from django.forms import ModelForm
from paciente.models import RegistroPaciente

class RegistroPacienteForm(ModelForm):
    """Formulario diseñado para registrar
    los datos de los pacientes del hospital
    """
    class Meta:
        model = RegistroPaciente

        fields = (
            'nombre',
            'apellido',
            'seg_nombre',
            'seg_apellido',
            'fecha_nacimiento',
            'letra_cedula_identidad',
            'cedula_identidad',
            'sexo',
            'pais',
            'estado',
            'municipio',
            'parroquia',
            'ciudad',
        )
        labels = {
            'nombre': 'Primer Nombre',
            'apellido': 'Primer Apellido',
            'seg_nombre': 'Segundo Nombre',
            'seg_apellido': 'Segundo Apellido',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'letra_cedula_identidad': 'Identidad',
            'cedula_identidad': 'Cédula Identidad',
            'sexo': 'Sexualidad',
            'pais': 'Nacionalidad',
            'estado': 'Estado-País',
            'municipio': 'Municipio',
            'parroquia': 'Parroquia',
            'ciudad': 'Ciudad',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'seg_nombre': forms.TextInput(attrs={'class':'form-control'}),
            'seg_apellido': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class':'form-control'}),
            'letra_cedula_identidad': forms.Select(attrs={'class':'form-control'}),
            'cedula_identidad': forms.NumberInput(attrs={'class':'form-control'}),
            'sexo': forms.Select(attrs={'class':'form-control'}),
            'pais': autocomplete.ModelSelect2(
                url='paciente:PaisAutoComplete',
                attrs={'class':'form-control select2'}),
            'estado': autocomplete.ModelSelect2(
                url='paciente:EstadoAutoComplete',
                attrs={'class':'form-control select2'}),
            'municipio' :autocomplete.ModelSelect2(
                url='paciente:MunicipioAutoComplete',
                attrs={'class':'form-control select2'}),
            'parroquia': autocomplete.ModelSelect2(
                url='paciente:ParroquiaAutoComplete',
                attrs={'class':'form-control select2'}),
            'ciudad': autocomplete.ModelSelect2(
                url='paciente:CiudadAutoComplete',
                attrs={'class':'form-control select2'}),
        }
        hola a todos