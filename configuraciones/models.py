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
		db_table = 'pregunta_secreta'
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
		db_table = 'sistema_aparato_biologico'
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
		db_table = 'listado_general_patologico'
		verbose_name = "Patologia"
		verbose_name_plural = "Patologias o Enfermedades"