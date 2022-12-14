from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_tienda.forms import *
from app_tienda.models import *
from app_perfiles.models import Avatar
from Tienda_online.settings import BASE_DIR
import os
from django.views.generic import ListView

# Create your views here.

def vista_inicio(request):
    if request.user.is_authenticated:
        imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")[0]
        imagen_url = imagen_model.imagen.url
    else:
        imagen_url = ""
    return render(request, "app_tienda/index.html", {"imagen_url": imagen_url})

def vista_nosotros(request):
    return render(request, "app_tienda/nosotros.html")

def vista_admin(request):
    return render(request, "app_tienda/editar_productos.html")



#? Falta el accesos por nivel de cuenta(Cliente, Empleado, Jefe)

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
    bebida = Bebidas.objects.all()
    salados = Salados.objects.all()
    pan_waf = Panqueques_Wafles.objects.all()
    contexto = {"cafes": cafes, "tortas": tortas, "bebida": bebida, "salados": salados, "pan_waf": pan_waf}
    return render(request, "app_tienda/menu.html", contexto)
    

def vista_eliminar_cafe(request, id):
    cafes = Cafe.objects.get(id=id)
    cafes.delete()
    return redirect("app_tienda-menu")

def vista_eliminar_torta(request, id):
    tortas = Torta.objects.get(id=id)
    tortas.delete()
    return redirect("app_tienda-menu")

def vista_eliminar_bebida(request, id):
    bebida = Bebidas.objects.get(id=id)
    bebida.delete()
    return redirect("app_tienda-menu")

def vista_eliminar_salados(request, id):
    salado = Salados.objects.get(id=id)
    salado.delete()
    return redirect("app_tienda-menu")

def vista_eliminar_panqueque_wafle(request, id):
    pan_waf = Panqueques_Wafles.objects.get(id=id)
    pan_waf.delete()
    return redirect("app_tienda-menu")

#? Falta Avatar y cambiar avatar

def vista_edit_cafe(request, id):
    
    cafes = Cafe.objects.get(id=id)

    if request.method == "POST":

        formulario = CafeForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            cafes.nombre_cafe = data["nombre_cafe"]
            cafes.precio = data["precio"]
            cafes.descripcion = data["descripcion"]

            cafes.save()

            return redirect("app_tienda-menu")

        else:
            return render(request, "app_tienda/editar_menu.html", {"formulario": formulario, "errores": formulario.errores})
    
    else:
        formulario = CafeForm(initial={"nombre_cafe":cafes.nombre_cafe, "precio":cafes.precio, "descripcion":cafes.descripcion})
    return render(request, "app_tienda/editar_menu.html", {"formulario": formulario, "nombre_cafe": ""})







def vista_edit_torta(request, id):
    
    tortas = Torta.objects.get(id=id)

    if request.method == "POST":

        formulario = TortaForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            tortas.nombre_torta = data["nombre_torta"]
            tortas.precio = data["precio"]
            tortas.descripcion = data["descripcion"]

            tortas.save()

            return redirect("app_tienda-menu")

        else:
            return render(request, "app_tienda/editar_menu.html", {"formulario": formulario, "errores": formulario.errores})
    
    else:
        formulario = TortaForm(initial={"nombre_torta":tortas.nombre_torta, "precio":tortas.precio, "descripcion":tortas.descripcion})
    return render(request, "app_tienda/editar_menu.html", {"formulario": formulario, "nombre_torta": ""})



def vista_edit_bebida(request, id):
    
    bebida = Bebidas.objects.get(id=id)

    if request.method == "POST":

        formulario = BebidasForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            bebida.nombre_bebida = data["nombre_bebida"]
            bebida.precio = data["precio"]

            bebida.save()

            return redirect("app_tienda-menu")

        else:
            return render(request, "app_tienda/editar_menu.html", {"formulario": formulario, "errores": formulario.errores})
    
    else:
        formulario = BebidasForm(initial={"nombre_bebida":bebida.nombre_bebida, "precio":bebida.precio})
    return render(request, "app_tienda/editar_menu.html", {"formulario": formulario, "nombre_bebida": ""})




def vista_edit_salados(request, id):
    
    salado = Salados.objects.get(id=id)

    if request.method == "POST":

        formulario = SaladosForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            salado.nombre_salados = data["nombre_salado"]
            salado.precio = data["precio"]

            salado.save()

            return redirect("app_tienda-menu")

        else:
            return render(request, "app_tienda/editar_menu.html", {"formulario": formulario, "errores": formulario.errores})
    
    else:
        formulario = SaladosForm(initial={"nombre_salado":salado.nombre_salados, "precio":salado.precio})
    return render(request, "app_tienda/editar_menu.html", {"formulario": formulario, "nombre_salado": ""})



def vista_edit_pw(request, id):
    
    pan_wd = Panqueques_Wafles.objects.get(id=id)

    if request.method == "POST":

        formulario = Panqueques_WaflesForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            pan_wd.nombre_PW = data["nombre_pan_waf"]
            pan_wd.precio = data["precio"]

            pan_wd.save()

            return redirect("app_tienda-menu")

        else:
            return render(request, "app_tienda/editar_menu.html", {"formulario": formulario, "errores": formulario.errores})
    
    else:
        formulario = Panqueques_WaflesForm(initial={"nombre_pan_wd":pan_wd.nombre_PW, "precio":pan_wd.precio})
    return render(request, "app_tienda/editar_menu.html", {"formulario": formulario, "nombre_pan_wd": ""})



def vista_tortas(request):
    if request.method == "POST":
        formulario = TortaForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            torta = Torta(nombre_torta = data["nombre_torta"], precio = data["precio"], descripcion = data["descripcion"])
            torta.save()
    formulario = TortaForm()
    return render(request,"app_tienda/tortas.html",  {"formulario": formulario})


def vista_bebidas(request):
    if request.method == "POST":
        formulario = BebidasForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            bebida = Bebidas(nombre_bebida = data["nombre_bebida"], precio = data["precio"])
            bebida.save()

    formulario = BebidasForm()
    return render(request, "app_tienda/bebidas.html", {"formulario" : formulario})


def vista_salados(request):
    if request.method == "POST":
        formulario = SaladosForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            salado = Salados( nombre_salados = data["nombre_salados"], precio = data["precio"])
            salado.save()

    formulario = SaladosForm()
    return render(request, "app_tienda/salados.html", {"formulario" : formulario})


def vista_panqueques_wafles(request):
    if request.method == "POST":
        formulario = Panqueques_WaflesForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            pan_waf = Panqueques_Wafles( nombre_PW = data["nombre_PW"], precio = data["precio"])
            pan_waf.save()

    formulario = Panqueques_WaflesForm()
    return render(request, "app_tienda/panqueques_wafles.html", {"formulario" : formulario})



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
            return render(request, "app_tienda/resultados_busqueda_cafe.html", {"lista_cafes": lista_cafes})
    return render(request, "app_tienda/busqueda.html", {"lista_cafes": []})



