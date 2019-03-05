from django.urls import path

from cuenta.views import Login

app_name = 'cuenta'
urlpatterns = [
    path( # Iniciar sesion, Registro de Usuario y Recuperar Cuenta
        'login/', 
        Login.as_view(
            template_name='login.html'
        ), 
        name='inicio-sesion'
    ),
]