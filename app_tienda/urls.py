from django.urls import path
from app_tienda.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("inicio/", vista_inicio, name = "app_tienda-inicio"),
    path("cafe/", vista_cafe, name = "app_tienda-cafe"),
    path("torta/", vista_tortas, name= "app_tienda-tortas"),
    path("busqueda/torta/",vista_resultado_torta, name="app_tienda-busqueda-torta"),
    path("busqueda/cafe/", vista_resultado_cafe, name="app_tienda-busqueda-cafe"),
    path("nosotros/", vista_nosotros, name = "app_tienda-nosotros"),

    #? usuario
    path("usuario/iniciar_session/", iniciar_sesion , name= "auth-login"),
    path("usuario/registrar/", registrar_usuario, name="auth-register"),
    path("usuario/logout/", LogoutView.as_view(template_name="app_tienda/logout.html"), name= "auth-logout"),

]