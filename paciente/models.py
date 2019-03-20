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
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    seg_nombre = models.CharField(max_length=80)
    seg_apellido = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField()
    letra_cedula_identidad = models.CharField('Letra C.I.', max_length=1, choices=LETRACEDULA_CHOICES, default=LETRACEDULA_CHOICES[0][0], blank=True, null=True)
    cedula_identidad = models.IntegerField("Cédula de Identidad", blank=True, null=True, db_index=True)
    sexo = models.CharField(max_length=255, choices=SEXO_CHOICES, blank=True, null=True)
    pais = models.ForeignKey('configuraciones.Pais', on_delete=models.PROTECT, db_index=True)
    estado = models.ForeignKey('configuraciones.Estado', on_delete=models.PROTECT, db_index=True)
    municipio = models.ForeignKey('configuraciones.Municipio', on_delete=models.PROTECT, db_index=True)
    parroquia = models.ForeignKey('configuraciones.Parroquia', on_delete=models.PROTECT, db_index=True)
    ciudad = models.ForeignKey('configuraciones.Ciudad', on_delete=models.PROTECT, db_index=True)
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name='fecha de registro')
    registro_actualizado = models.DateTimeField(auto_now=True, verbose_name='fecha de actualizacion')

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)
    
    class Meta:
        ordering = ['nombre']
        db_table = 'paciente\".\"registro_paciente'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
