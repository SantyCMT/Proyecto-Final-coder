from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from app_perfiles.forms import *
from app_perfiles.models import Avatar

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

def registrar_usuario(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            
            formulario.save()
            return redirect("app_tienda-inicio")

        else:
            return render(request, "app_perfiles/register.html", {"form" : formulario, "errors" : formulario.errors})

    formulario = UserRegisterForm()
    return render(request, "app_perfiles/register.html", {"form" : formulario})


def iniciar_sesion(request):

    errors = ""

    if request.method == "POST":
        formulario = AuthenticationForm( request, data= request.POST )

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username= data["username"], password= data["password"])

            if user is not None:
                login(request, user)
                return redirect("app_tienda-inicio")
            else:
                return render (request, "app_perfiles/login.html",{"form":formulario, "errors" : "Credeciales invalidas"})
        
        else:
            return render(request, "app_perfiles/login.html", {"form":formulario, "errors" : formulario.errors})

    formulario = AuthenticationForm()
    return render(request, "app_perfiles/login.html",{"form" : formulario, "errors" : errors})


@login_required
def edit_perfil(request):
    usuario = request.user

    if request.method == "POST":

        formulario = UserEditForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data ["email"]

            usuario.save()
            return redirect("app_tienda-inicio")
        else:
            return render(request, "app_perfiles/edit_perfil.html", {"form": formulario, "erros": formulario.errors})

    else:

        formulario = UserEditForm(initial = {"email": usuario.email,"first_name": usuario.first_name, "last_name": usuario.last_name})

    return render(request, "app_perfiles/edit_perfil.html", {"form": formulario})



@login_required
def avatar_user(request):

    if request.method == "POST":
        formulario = AvatarForm(request.POST, files= request.FILES)
        print(request.FILES, request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario = request.user

            avatar = Avatar(user=usuario, imagen = data["imagen"])
            avatar.save()

            return redirect("app_tienda-inicio")
        else:
            return render(request, "app_perfiles/agregar_avatar.html", {"form": formulario, "errors": formulario.errors})
        
    formulario = AvatarForm()

    return render(request, "app_perfiles/agregar_avatar.html", {"form": formulario})