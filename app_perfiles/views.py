from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from app_perfiles.forms import *
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