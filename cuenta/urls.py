from django.urls import path

from cuenta.views import Login

app_name = 'cuenta'
urlpatterns = [
    path( # Iniciar sesion utilizando materialize
        'login/', 
        Login.as_view(
            template_name='login.html'
        ), 
        name='inicio-sesion'
    ),
    path(#Registro de Nuevos Usuarios
        'login/nuevo-registro/',
        Login.as_view(
            template_name='registro_usuario.html'
        ), 
        name='registro-de-usuario'
    ),
    path(
        'login/recuperar/', 
        Login.as_view(
            template_name='recuperar_cuenta.html'
        ), 
        name='recuperar-cuenta'
    )
]