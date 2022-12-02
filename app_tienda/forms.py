from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()
    nombre_usuario = forms.CharField()
    contrasenia = forms.CharField()

class CafeForm(forms.Form):
    nombre_cafe = forms.CharField()
    precio = forms.IntegerField()
    descripcion = forms.CharField()

class TortaForm(forms.Form):
     nombre_torta = forms.CharField()
     precio = forms.IntegerField()
     descripcion = forms.CharField()
     