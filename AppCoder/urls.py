from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="home"),
    path("profesores" , views.profesores , name="profesores"),
    path("cursos" , views.cursos , name="cursos"),
    path("alumnos" , views.alumnos , name="alumnos" ),
    #path("contacto" , views.contacto),
    #path("alta_curso/<nombre>" , views.alta_curso),
    path("alta_curso" , views.curso_formulario),
    path("buscar_curso" , views.buscar_curso),
    path("buscar" , views.buscar),
    path("eliminar_curso/<int:id>" , views.eliminar_curso , name="eliminar_curso"),
    path("editar_curso/<int:id>" , views.editar , name="editar_curso"),
    path("editar_curso" , views.editar ,name="editar_curso"),
    path("login",views.login_request,name="Login"),
    path("logout",LogoutView.as_view(template_name="logout.html"),name="Logout"),
    path("register",views.register,name="Register"),
    path("editarPerfil",views.editarPerfil, name="EditarPerfil")
  
]