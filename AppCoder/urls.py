from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="home"),
    path("profesores" , views.profesores , name="profesores"),
    path("cursos" , views.cursos , name="cursos"),
    path("alumnos" , views.alumnos , name="alumnos" ),
    #cursos
    path("alta_curso" , views.curso_formulario),
    path("buscar_curso" , views.buscar_curso),
    path("buscar" , views.buscar),
    path("eliminar_curso/<int:id>" , views.eliminar_curso , name="eliminar_curso"),
    path("editar_curso/<int:id>" , views.editar , name="editar_curso"),
    path("editar_curso" , views.editar ,name="editar_curso"),
    path("login",views.login_request,name="Login"),
    path("logout",LogoutView.as_view(template_name="logout.html"),name="Logout"),
    path("register",views.register,name="Register"),
    path("editarPerfil",views.editarPerfil, name="EditarPerfil"),
    #alumnos
    path("alta_alumno", views.alumno_formulario),
    path("buscar_alumno" , views.buscar_alumno),
    path("buscar2" , views.buscar2),
    path("eliminar_alumno/<int:id>", views.eliminar_alumno, name="eliminar_alumno"),
    path("editar_alumno/<int:id>" , views.editar_alumno , name="editar_alumno"),
    path("editar_alumno" , views.editar_alumno ,name="editar_alumno")
    #profesores
    #path("alta_profesor",views.profesor_formulario),
    # path("buscar_profesor" , views.buscar_profesor),
    # path("eliminar_profesor/<int:id>", views.eliminar_profesor, name="eliminar_profesor"),
    # path("editar_profesor/<int:id>" , views.editar , name="editar_profesor"),
    # path("editar_profesor" , views.editar ,name="editar_profesor")
]