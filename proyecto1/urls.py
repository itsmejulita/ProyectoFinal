"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from AppKF.views import *
from django.urls import path
from AppKF.views import ListaHeladeria, DetalleHeladeria, CrearHeladeria, ActualizarHeladeria, BorrarHeladeria
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [ 

    path('admin/', admin.site.urls),
    path("nueva_vinoteca/", agregar_vinos),
    path("Vinoteca/", ver_vinos, name="Vinos"),
    path("formu/", agregar_vinos),
    path("inicio/", inicio, name="Inicio"),
    path("nueva_cafeteria/", cafeteria_1),
    path("cafeteria_1/", ver_cafeteria, name="Café"),
    path("formu/", cafeteria_1),
    path("nueva_heladeria/", agregar_helados),
    path("Heladeria/", ver_helados, name="Helados"), 
    path('cursoFormulario/', curso_formulario, name='FormularioCurso'),
    path("buscarCamada/", busquedaCamada, name="BuscarCamada"),
    path("buscar/", buscar, name="ResultadoCamada"),
    path("login/", inicioSesion, name="Login"),
    path("register/", registro, name="Registro"),
    path("logout/", LogoutView.as_view (template_name = "logout.html"), name = "Logout"), 
    path("editarUsuario/", EditarUsuario, name = "EditarUsuario"),
    path("avatar/", agregarAvatar, name = "Avataragregar"),



    #CRUD DE CAFÉ USANDO CLASES: 
    path ("Coffe/", include([
        path ("list/", ListaCafe.as_view(), name="Cafeleer"),
        path ("<int:pk>", DetalleCafe.as_view(), name="Cafedetalle"),
        path ("crear", Crearcoffe.as_view(), name="Cafecrear"),
        path ("borrar/<int:pk>", Borrarcoffe.as_view(), name="Cafeborrar"),
        path ("editar/<int:pk>", Actualizarcoffe.as_view(), name="Cafeeditar"),
    ])),

    #CRUD DE HELADERIA USANDO CLASES: 
    path ('Heladeria/', include([   
        path ('list/', ListaHeladeria.as_view(), name='Heladerialeer'),
        path ('<int:pk>', DetalleHeladeria.as_view(), name='Heladeriadetalle'),
        path ('crear', CrearHeladeria.as_view(), name='Heladeriacrear'),
        path ('editar/<int:pk>', ActualizarHeladeria.as_view(), name='Heladeriaeditar'),
        path ('borrar/<int:pk>', BorrarHeladeria.as_view(), name='Heladeriaborrar'), 
    ])),

    #CRUD DE VINOS:
    path ("vinos/", include([
        path ("leer/", leerVinos, name="Vinosleer"),
        path ("crear/", crearVinos, name="Vinoscrear"),
        path ("eliminar/<vinosNombre>/", eliminar, name="Vinoseliminar"), 
        path ("editar/<vinosNombre>/", editar, name="Vinoseditar"),
    ]))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)