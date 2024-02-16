from django.shortcuts import render
from AppKF.forms import *
from AppKF.models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 

# Vista de Inicio de Sesión 
def inicio (request):
    
    return render(request,"inicio.html", {"mensaje": "Bienvenido a mi pagina Web! "})

def inicioSesion(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            info = form.cleaned_data

            usuario = info["username"]
            contraseña = info["password"]

            user = authenticate(username = usuario, password = contraseña)

            if user is not None: 

                login(request, user)

                return render(request, "inicio.html", {"mensaje" : f"Bienvenido {user}"})

            else:
                
                return render(request, "inicio.html", {"mensaje": "Datos incorrectos."})
    
    else:
        form = AuthenticationForm()

    return render(request,"login.html", {"formulario": form})

def registro(request):

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]

            form.save()

            return render(request, "inicio.html", {"mensaje": "Usuario creado"})
    else:
        form = LoginForm()

    return render(request, "registro.html", {"formulario": form})


def EditarUsuario(request):
    
    usuario = request.user 

    if request.method == "POST":
        form = FormularioEditar(request.POST)
        if form.is_valid():
            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "inicio.html")
    else:
        form = FormularioEditar(initial={
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name,
        })

    return render(request, "editarPerfil.html", {"formulario": form, "usuario": usuario})

@login_required
def agregarAvatar(request):

    if request.method=="POST":

        form = AvatarFormulario(request.POST, request.Files)

        if form.is_valid():
            
            usuarioActual = User.object.get(username=request.user)

            avatar = Avatar(usuario=usuarioActual, imagen = form.cleaned_data["imagen"])

            avatar.save()

            return render(request, "inicio.html")
        
    else:
        form = AvatarFormulario()

    return render(request, "agregarAvatar.html", {"formulario": form})


def agregar_vinos(request):
    if request.method == "POST":
        # VAMOS A GUARDAR LA INFO
        info_formulario = Vinosform (request.POST)

        if info_formulario.is_valid():

            info = info_formulario.cleaned_data
            nueva_vinoteca = Vinoteca(nombre= info["nombre"], empresa = info["empresa"], año = info["año"])

            nueva_vinoteca.save()
            
            return render (request,"todos_los_vinos.html") 

        
    else: 
        nuevo_formulario = Vinosform()

    return render(request, "crear_vinos.html", {"formu": nuevo_formulario}) # Formu es lo que va a leer el html

def ver_vinos(request): 
    vinos = Vinoteca.objects.all()
    return render(request, "todos_los_vinos.html", {"vinos": vinos}) 

####################################################################################################

def cafeteria_1 (request): 
    if request.method == "POST":
        # VAMOS A GUARDAR LA INFO  
        info_formulario = cafeteriaForm(request.POST)


        if info_formulario.is_valid():
            info = info_formulario.cleaned_data

            nueva_cafeteria = Cafeteria(nombre = info["nombre"], apellido = info["apellido"], fecha = info["fecha"])

            nueva_cafeteria.save()
            return render(request, "todas_las_cafeterias.html") 
    else: 
        nuevo_formulario = cafeteriaForm()
    return render(request, "crear_cafeteria.html", {"formu": nuevo_formulario}) # Formu es lo que va a leer el html


def ver_cafeteria(request): 
    cafeterias = Cafeteria.objects.all()
    return render(request, "todos_los_cafes.html", {"cafeterias": cafeterias})

####################################################################################################

def agregar_helados(request):
    if request.method == "POST":
        # VAMOS A GUARDAR LA INFO
        info_formulario = heladeriaForm(request.POST)

        if info_formulario.is_valid():
            info = info_formulario.cleaned_data
            nueva_heladeria = Heladeria(nombre=info["nombre"], producto=info["producto"], cantidad=info["cantidad"])
            nueva_heladeria.save()
            
            return render(request, "todos_los_helados.html") 

    else: 
        nuevo_formulario = heladeriaForm()

    return render(request, "crear_helados.html", {"formu": nuevo_formulario}) # Formu es lo que va a leer el html

def ver_helados(request): 
    heladerias = Heladeria.objects.all()
    return render(request, "todos_los_helados.html", {"heladerias": heladerias})


def curso_formulario(request):

    if request.method == "POST":
        formulario = CursoForm(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data
            curso = Curso(nombre=info["Curso"], camada=info["Camada"])
            curso.save()
            return redirect("inicio.html")  # Redirige a la página de inicio

    else:
        formulario = CursoForm()  # Inicializa el formulario

    return render(request, "cursoFormulario.html", {"form1": formulario})

def busquedaCamada(request):
    return render(request, "inicio.html")

def buscar(request):
    if 'camada' in request.GET and request.GET["camada"]:
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__iexact= camada)
        return render(request, "resultados.html", {"cursos": cursos})
    else:
        if 'Curso' in request.GET and request.GET["Curso"]:
            curso = request.GET["Curso"]
            return render(request, "inicio.html", {"Curso": curso})
        else:
            respuesta = "No enviaste datos"
            return HttpResponse(respuesta) 
@login_required
def leerVinos(request):

    Vinos = Vinoteca.objects.all()
    contexto = {"wine": Vinos}
    return render(request, "leerVinos.html", contexto)

def crearVinos(request):
    formulario1 = Vinosform()  # Inicializa el formulario
    if request.method == "POST": 
        formulario1 = Vinosform(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            vinos_info = Vinoteca(nombre = info["nombre"], empresa = info["empresa"], año = info["año"])
            vinos_info.save()
            return render(request, "inicio.html")
    else:
        formulario1 = Vinosform()
        return render(request, "Vinosform.html", {"form1": formulario1})
    
def eliminar(request, vinosNombre):
    
    nombreV = Vinoteca.objects.get(nombre=vinosNombre)
    nombreV.delete()
    nombreV = Vinoteca.objects.all()
    contexto = {"name" : nombreV}
    return render (request, "leerVinos.html", contexto)


def editar(request, vinosNombre): 
    nombreV = Vinoteca.objects.get(nombre=vinosNombre)

    if request.method =="POST":
        formulario1 = Vinosform(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data

            nombreV.nombre = info ["nombre"]
            nombreV.empresa = info ["empresa"]
            nombreV.año = info ["año"]
            nombreV.save()
            return render(request, "inicio.html")
    else:
        formulario1 = Vinosform(initial={"nombre": nombreV.nombre, "empresa": nombreV.empresa,"año": nombreV.año})
        return render(request, "editar.html", {"form1": formulario1, "nombre": vinosNombre})

class ListaCafe(LoginRequiredMixin, ListView):

    model = Cafeteria

class DetalleCafe(LoginRequiredMixin, DetailView):

    model = Cafeteria 

class Crearcoffe(LoginRequiredMixin, CreateView):
    model = Cafeteria
    success_url = reverse_lazy('Cafeleer')
    fields = ["nombre", "apellido", "fecha"]

class Actualizarcoffe(LoginRequiredMixin, UpdateView):
    model = Cafeteria
    success_url = reverse_lazy('Cafeleer')
    fields = ["nombre", "apellido", "fecha"]

class Borrarcoffe(LoginRequiredMixin, DeleteView):
    model = Cafeteria
    success_url = reverse_lazy('Cafeleer')


class ListaHeladeria(LoginRequiredMixin, ListView):
    model = Heladeria
    template_name = 'AppKF/heladeria_list.html'

class DetalleHeladeria(LoginRequiredMixin, DetailView):
    model = Heladeria
    template_name = 'AppKF/heladeria_detail.html'

class CrearHeladeria(LoginRequiredMixin, CreateView):
    model = Heladeria
    template_name = 'AppKF/heladeria_form.html'
    fields = '__all__'

class ActualizarHeladeria(LoginRequiredMixin, UpdateView):
    model = Heladeria
    template_name = 'AppKF/heladeria_form.html'
    fields = '__all__'

class BorrarHeladeria(LoginRequiredMixin, DeleteView):
    model = Heladeria
    template_name = 'AppKF/heladeria_confirm_delete.html'
    success_url = '/Heladeria/list/'


    