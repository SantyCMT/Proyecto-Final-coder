from django.urls import path
from app_tienda.views import *

urlpatterns = [
    path("inicio/", vista_inicio, name = "app_tienda-inicio"),
    path("registro/", vista_registro, name = "app_tienda-registro"),
    path("cafe/", vista_cafe, name = "app_tienda-cafe"),
    path("torta/", vista_tortas, name= "app_tienda-tortas"),
    path("iniciar_sesion/", vista_inicio_sesion, name="app_tienda-iniciar-sesion"),
    path("busqueda/torta/",vista_resultado_torta, name="app_tienda-busqueda-torta"),
    path("busqueda/cafe/", vista_resultado_cafe, name="app_tienda-busqueda-cafe"),
    path("nosotros/", vista_nosotros, name = "app_tienda-nosotros"),

]