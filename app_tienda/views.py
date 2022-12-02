from django.shortcuts import render, redirect
from app_tienda.forms import *
from app_tienda.models import *

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
# Create your views here.

def vista_inicio(request):
    return render(request, "app_tienda/index.html")

def vista_nosotros(request):
    return render(request, "app_tienda/nosotros.html")

def vista_registro(request):
    if request.method == "POST":
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            user = Usuario(nombre = data["nombre"], apellido = data["apellido"], edad = data["edad"], email = data["email"], nombre_usuario = data["nombre_usuario"], contrasenia = data["contrasenia"])
            user.save()
    formulario = UsuarioForm()
    return render(request, "app_tienda/registro.html", {"formulario": formulario})

def vista_cafe(request):
    if request.method == "POST":
        formulario = CafeForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            cafe = Cafe(nombre_cafe = data["nombre_cafe"], precio = data["precio"], descripcion = data["descripcion"])
            cafe.save()
    formulario = CafeForm()
    return render(request, "app_tienda/cafe.html" , {"formulario": formulario})

def vista_tortas(request):
    if request.method == "POST":
        formulario = TortaForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            torta = Torta(nombre_torta = data["nombre_torta"], precio = data["precio"], descripcion = data["descripcion"])
            torta.save()
    formulario = TortaForm()
    return render(request,"app_tienda/tortas.html",  {"formulario": formulario})

def vista_inicio_sesion(request):
    return render(request, "app_tienda/iniciar_sesion.html")

def vista_busqueda(request):
    return render(request, "app_tienda/busqueda.html")

def vista_resultado_torta(request):
    if request.GET:
        name_torta = request.GET.get("nombre_torta", "")
        if name_torta == "":
            lista_torta = []

        else:
            lista_torta = Torta.objects.filter(nombre_torta=name_torta)
            return render(request, "app_tienda/resultados_busqueda_torta.html", {"lista_de_torta": lista_torta})
    return render(request, "app_tienda/busqueda.html", {"lista_de_torta": []})


def vista_resultado_cafe(request):
    if request.GET:
        name_cafe = request.GET.get("nombre_cafe", "")
        if name_cafe == "":
            lista_cafes = []

        else:
            lista_cafes = Cafe.objects.filter(nombre_cafe=name_cafe)
            return render(request, "app_tienda/resultados_busqueda_cafe.html", {"lista_de_cafes": lista_cafes})
    return render(request, "app_tienda/busqueda.html", {"lista_de_cafe": []})


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
                return render (request, "app_tienda/login.html",{"form":formulario, "errors" : "Credeciales invalidas"})
        
        else:
            return render(request, "app_tienda/login.html", {"form":formulario, "errors" : formulario.errors})

    formulario = AuthenticationForm()
    return render(request, "app_tienda/login.html",{"form" : formulario, "errors" : errors})


def registrar_usuario(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            
            formulario.save()
            return redirect("app_tienda-inicio")

        else:
            return render(request, "app_tienda/register.html", {"form" : formulario, "errors" : formulario.errors})

    formulario = UserRegisterForm()
    return render(request, "app_tienda/register.html", {"form" : formulario})
