# Librerias Future
from __future__ import unicode_literals

# Librerias Django
from django.db import models

class PreguntaSecreta(models.Model):
	'''Modelo Creado para agregar las preguntas secretas
	que se tomaran en cuenta a la hora de hacer un registro
	de usuario y esto lo llevara el rol Admin
	'''
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ['nombre']
		db_table = 'configuracion\".\"pregunta_secreta'
		verbose_name = "Pregunta Secreta"
		verbose_name_plural = "Preguntas Secretas"


class SistemaAparatoBiologico(models.Model):
	'''Se refiere a la division del cuerpo humano
	y se toma como secciones independiente y grupales
	de los aparatos que se encuentran en el cuerpo
	'''
	nombre_aparato = models.CharField(max_length=150)


	def __str__(self):
		return self.nombre_aparato
	
	class Meta:
		ordering = ['nombre_aparato']
		db_table = 'configuracion\".\"sistema_aparato_biologico'
		verbose_name = "Sistema o Aparato Biologico"
		verbose_name_plural = "Sistema o Aparato Biologico"
	

class PatologiasGenerales(models.Model):
	'''Modelo que sirve para almacenar todos los tipos de
	enfermedades comunes que presentan los pacientes
	'''
	'''Estoy asociando mi llave primaria id de la
	tabla SistemaAparatoBiologico con la llave foranea
	aparato_biologico haciendo referencia al nombre de la
	tabla padre
	'''
	aparato_biologico = models.ForeignKey(
		'SistemaAparatoBiologico', on_delete=models.PROTECT, db_index=True)
	nombre_patologico = models.CharField(max_length=150)


	def __str__(self):
		return self.nombre_patologico

	class Meta:
		ordering = ['nombre_patologico']
		db_table = 'configuracion\".\"listado_general_patologico'
		verbose_name = "Patologia"
		verbose_name_plural = "Patologias o Enfermedades"


class Pais(models.Model):
	'''Nombre del pais de residencia
	'''
	nombre_pais = models.CharField(max_length=60)

	def __str__(self):
		return self.nombre_pais
	
	class Meta:
		ordering = ['nombre_pais']
		db_table = 'configuracion\".\"pais_nacion'
		verbose_name = 'Pais Nacion'
		verbose_name_plural = 'Nacionalidad'


class Estado(models.Model):
	'''Estado geografico que pertenece el paciente
	'''
	pais = models.ForeignKey(
		'Pais', on_delete=models.PROTECT, db_index=True)
	nombre_estado = models.CharField(max_length=150)

	def __str__(self):
		return self.nombre_estado
	
	class Meta:
		ordering = ['nombre_estado']
		db_table = 'configuracion\".\"estado_nacion'
		verbose_name = 'Estado'
		verbose_name_plural = 'Estados de la Nacion'


class Municipio(models.Model):
	'''a que municipio pertenece el paciente
	'''
	estado = models.ForeignKey(
		'Estado', on_delete=models.PROTECT, db_index=True)
	nombre_municipio = models.CharField(max_length=255)

	def __str__(self):
		return self.nombre_municipio
	
	class Meta:
		ordering = ['nombre_municipio']
		db_table = 'configuracion\".\"municipio_nacion'
		verbose_name = 'Municipio'
		verbose_name_plural = 'Municipios de la Nacion'


class Parroquia(models.Model):
	'''Parroquia a la que pertenece el municipio
	donde vive el paciente
	'''
	municipio = models.ForeignKey(
		'Municipio', on_delete=models.PROTECT, db_index=True)
	nombre_parroquia = models.CharField(max_length=255)

	def __str__(self):
		return self.nombre_parroquia

	class Meta:
		ordering = ['nombre_parroquia']
		db_table = 'configuracion\".\"parroquia_nacion'
		verbose_name = 'Parroquia'
		verbose_name_plural = 'Parroquias de la Nacion'


class Ciudad(models.Model):
	'''Donde habita la vivienda del paciente
	'''
	municipio = models.ForeignKey(
		'Municipio', on_delete=models.PROTECT, db_index=True)
	nombre_ciudad = models.CharField(max_length=255)

	def __str__(self):
		return self.nombre_ciudad
	
	class Meta:
		ordering = ['nombre_ciudad']
		db_table = 'configuracion\".\"ciudad_nacion'
		verbose_name = 'Ciudad'
		verbose_name_plural = 'Ciudades de la Nacion'

