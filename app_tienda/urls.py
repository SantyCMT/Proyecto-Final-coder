from django.urls import path,include
from app_tienda.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", vista_inicio, name = "app_tienda-inicio"),
    path("editar/", vista_admin, name= "app_tienda-vista-admin"),
    path("cafe/", vista_cafe, name = "app_tienda-cafe"),
    path("torta/", vista_tortas, name= "app_tienda-tortas"),
    path("bebida/", vista_bebidas, name= "app_tienda-bebidas"),
    path("salados/", vista_salados, name= "app_tienda-salados"),
    path("panqueques_wafles/", vista_panqueques_wafles, name= "app_tienda-panqueques_wafles"),
    path("menu/", vista_menu_cafes, name= "app_tienda-menu"),
    path("menu/borrar/<id>/", vista_eliminar_cafe, name= "app_tienda-borrar-menu"),
    path("menu/borrar/torta/<id>/", vista_eliminar_torta, name= "app_tienda-borrar-menu-torta"),
    path("menu/borrar/bebida/<id>/", vista_eliminar_bebida, name= "app_tienda-borrar-menu-bebida"),
    path("menu/borrar/salados/<id>/", vista_eliminar_salados, name= "app_tienda-borrar-menu-salados"),
    path("menu/borrar/panqueques_wafles/<id>/", vista_eliminar_panqueque_wafle, name= "app_tienda-borrar-menu-pan_waf"),
    path("menu/editar/<id>/", vista_edit_menu, name= "app_tienda-editar-menu"),
    path("busqueda/torta/",vista_resultado_torta, name="app_tienda-busqueda-torta"),
    path("busqueda/cafe/", vista_resultado_cafe, name="app_tienda-busqueda-cafe"),
    path("nosotros/", vista_nosotros, name = "app_tienda-nosotros"),
    path('usuarios/', include("app_perfiles.urls"))


]