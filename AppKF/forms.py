from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppKF.models import Avatar

class Vinosform(forms.Form):

    nombre = forms.CharField(max_length=30)
    empresa = forms.CharField(max_length=30)
    año = forms.IntegerField()

class cafeteriaForm(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    fecha = forms.IntegerField()

class heladeriaForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    producto = forms.CharField(max_length=30)
    cantidad = forms.IntegerField()

class CursoForm(forms.Form):
    Curso = forms.CharField(max_length=30)
    Camada = forms.CharField() 


class LoginForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(label = "Username")
    password1 = forms.CharField(label = "Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Password", widget=forms.PasswordInput)

class Meta:

    model = User 
    fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email', 'password1', 'password2']

class FormularioEditar(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','first_name','last_name', 'password1', 'password2'] 


class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar 
        fields = ["imagen"]
    

    