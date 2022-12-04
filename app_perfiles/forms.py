from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    nombre_usuario = forms.CharField(label= "Nombre")
    apellido_usuario =  forms.CharField(label= "Apellido")
    email = forms.EmailField(label= "Correo electronico ")
    password1 =  forms.CharField(label= "Contraseña",  widget =  forms.PasswordInput)
    password2 =  forms.CharField(label= "Repetir contraseña",  widget =  forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "nombre_usuario", "apellido_usuario", "password1", "password2"]
        help_texts = { k: "" for k in fields}

