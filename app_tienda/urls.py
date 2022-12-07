from django.urls import path,include
from app_tienda.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", vista_inicio, name = "app_tienda-inicio"),
    path("cafe/", vista_cafe, name = "app_tienda-cafe"),
    path("torta/", vista_tortas, name= "app_tienda-tortas"),
    path("menu/", vista_menu_cafes, name= "app_tienda-menu"),
    path("menu/borrar/<id>/", vista_eliminar, name= "app_tienda-borrar-menu"),
    path("menu/borrar/torta/<id>/", vista_eliminar_torta, name= "app_tienda-borrar-menu-torta"),
    path("busqueda/torta/",vista_resultado_torta, name="app_tienda-busqueda-torta"),
    path("busqueda/cafe/", vista_resultado_cafe, name="app_tienda-busqueda-cafe"),
    path("nosotros/", vista_nosotros, name = "app_tienda-nosotros"),
    path('usuarios/', include("app_perfiles.urls"))


]