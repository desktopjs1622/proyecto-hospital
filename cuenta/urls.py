from django.urls import path

from cuenta.views import Login

app_name = 'cuenta'
urlpatterns = [
    path( #Iniciar la sesión utilizando bootstrap
        'login/', 
        Login.as_view(
            template_name='login.html'
        ), 
        name='inicio-sesion'
    ),
    path(# Iniciar sesion utilizando materialize
        'login2/', 
        Login.as_view(
            template_name='login2.html'
        ), 
        name='login'
    ),
    path(#Registro de Nuevos Usuarios
        'registro_usuario/',
        Login.as_view(
            template_name='registro_usuario.html'
        ), 
        name='registro-de-usuario'
    ),
    path(
        'recuperar_cuenta/', 
        Login.as_view(
            template_name='recuperar_cuenta.html'
        ), 
        name='recuperar-cuenta'
    )
]