from django.db import models
from django.utils import timezone


class RegistroPaciente(models.Model):
    '''Modelo para el registro de los pacientes
    que solicitan servicios de salud y que por medio
    de estos datos se le puedan anexar a la historia
    médica sea adulto, joven, niño y anciano
    '''
    SEXO_CHOICES = (
        ('F', 'FEMENINO'),
        ('M', 'MASCULINO'),
    )
    LETRACEDULA_CHOICES = (
        ('V', 'V'),
        ('E', 'E'),
    )
    nombre = models.CharField(max_length=80, null=False, blank=False)
    apellido = models.CharField(max_length=80, null=False, blank=False)
    seg_nombre = models.CharField(max_length=80)
    seg_apellido = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField()
    letra_cedula_identidad = models.CharField('Letra C.I.', max_length=1, choices=LETRACEDULA_CHOICES, default=LETRACEDULA_CHOICES[0][0], blank=False, null=False)
    cedula_identidad = models.IntegerField("Cédula de Identidad", blank=False, db_index=True, null=False)
    sexo = models.CharField(max_length=255, choices=SEXO_CHOICES, blank=False, null=False)
    nombre_pais = models.ForeignKey('configuraciones.Pais', on_delete=models.CASCADE, blank=False, null=False)
    nombre_estado = models.ForeignKey('configuraciones.Estado', on_delete=models.CASCADE, blank=False, null=False)
    nombre_municipio = models.ForeignKey('configuraciones.Municipio', on_delete=models.CASCADE, blank=False, null=False)
    nombre_parroquia = models.ForeignKey('configuraciones.Parroquia', on_delete=models.CASCADE, blank=False, null=False)
    nombre_ciudad = models.ForeignKey('configuraciones.Ciudad', on_delete=models.CASCADE, blank=False, null=False)
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name='fecha de registro')
    registro_actualizado = models.DateTimeField(auto_now=True, verbose_name='fecha de actualizacion')

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)
    
    class Meta:
        ordering = ['nombre']
        db_table = 'paciente\".\"registro_paciente'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
