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
            'nombre_pais',
            'nombre_estado',
            'nombre_municipio',
            'nombre_parroquia',
            'nombre_ciudad',
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
            'nombre_pais': 'Nacionalidad',
            'nombre_estado': 'Estado-País',
            'nombre_municipio': 'Municipio',
            'nombre_parroquia': 'Parroquia',
            'nombre_ciudad': 'Ciudad',
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
            'nombre_pais': autocomplete.ModelSelect2(
                url='configuraciones:PaisAutoComplete',
                attrs={'class':'form-control select2'}),
            'nombre_estado': autocomplete.ModelSelect2(
                url='configuraciones:EstadoAutoComplete',
                attrs={'class':'form-control select2'}),
            'nombre_municipio' :autocomplete.ModelSelect2(
                url='configuraciones:MunicipioAutoComplete',
                attrs={'class':'form-control select2'}),
            'nombre_parroquia': autocomplete.ModelSelect2(
                url='configuraciones:ParroquiaAutoComplete',
                attrs={'class':'form-control select2'}),
            'nombre_ciudad': autocomplete.ModelSelect2(
                url='configuraciones:CiudadAutoComplete',
                attrs={'class':'form-control select2'}),
        }