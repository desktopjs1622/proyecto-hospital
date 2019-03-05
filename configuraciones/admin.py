from django.contrib import admin

'''Usamos los modelos que se encuentran en
la apps y se menciona de donde se esta llamando
dicho modelo
'''
from configuraciones.models import PreguntaSecreta, PatologiasGenerales

'''Para que el administrador de Django muestre el
modelo creado se llamara de la siguiente manera
'''

'''Creado para administrar las preguntas secretas
'''
admin.site.register(PreguntaSecreta)

'''Creado para registrar los distintos tipos de 
patologias o enfermedades que se tienen como cono
cimientos y las nuevas enfermedades
'''
admin.site.register(PatologiasGenerales)