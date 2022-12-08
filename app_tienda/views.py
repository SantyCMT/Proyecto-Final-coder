from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_tienda.forms import *
from app_tienda.models import *

# Create your views here.

def vista_inicio(request):
    return render(request, "app_tienda/index.html")

def vista_nosotros(request):
    return render(request, "app_tienda/nosotros.html")

def vista_cafe(request):
    if request.method == "POST":
        formulario = CafeForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            cafe = Cafe(nombre_cafe = data["nombre_cafe"], precio = data["precio"], descripcion = data["descripcion"])
            cafe.save()
    formulario = CafeForm()
    return render(request, "app_tienda/cafe.html" , {"formulario": formulario})
    

def vista_menu_cafes(request):
    cafes = Cafe.objects.all()
    tortas = Torta.objects.all()
    contexto = {"cafes": cafes, "tortas": tortas}
    return render(request, "app_tienda/menu.html", contexto)
    

def vista_eliminar_cafe(request, id):
    cafes = Cafe.objects.get(id=id)
    cafes.delete()
    return redirect("app_tienda-menu")

def vista_eliminar_torta(request, id):
    tortas = Torta.objects.get(id=id)
    tortas.delete()
    return redirect("app_tienda-menu")

def vista_edit_menu(request, id):
    cafes = Cafe.objects.get(id=id)

    if request.method == "POST":
        formulario = CafeForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            cafes.nombre_cafe = data["nombre_cafe"]
            cafes.precio = data["precio"]
            cafes.descripcion = data ["descripcion"]
            cafes.save()
            return redirect("app_tienda-menu")
        else:
            return render(request, "app_tienda/menu.html", {"formulario": formulario, "errores": formulario.errores})
    
    else:
        formulario = CafeForm(initial={"nombre":cafes.nombre_cafe, "precio":cafes.precio, "descripcion":cafes.descripcion})
        return render(request, "app_tienda/menu.html", {"formulario": formulario, "errores": ""})


def vista_tortas(request):
    if request.method == "POST":
        formulario = TortaForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            torta = Torta(nombre_torta = data["nombre_torta"], precio = data["precio"], descripcion = data["descripcion"])
            torta.save()
    formulario = TortaForm()
    return render(request,"app_tienda/tortas.html",  {"formulario": formulario})


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



