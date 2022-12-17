from django.urls import path
from app_perfiles.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [

    #? usuario
    path("iniciar_session/", iniciar_sesion , name= "auth-login"),
    path("registrar/", registrar_usuario, name="auth-register"),
    path("logout/", LogoutView.as_view(template_name="app_perfiles/logout.html"), name= "auth-logout"),
    path("edit_profile", edit_perfil, name="auth-edit_profile" ),
    path("add_avatar/", avatar_user, name= "auth-add_avatar")

]
