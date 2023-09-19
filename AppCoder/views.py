from django.shortcuts import render
from AppCoder.models import Curso, Avatar, Profesores, Alumnos
from django.template import loader
from django.http import HttpResponse
from AppCoder.forms import Curso_form, UserEditForm, Alumnos_form, Profesores_form
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def inicio(request):
    print(request.user.id)
    if request.user.id != None:
        avatares = Avatar.objects.filter(user=request.user.id)
        return render( request , "padre.html", {"url":avatares[0].imagen.url})
    else:
        return render( request , "padre.html")

def cursos(request):
    print(request.user.id)
    if request.user.id != None:
        avatares = Avatar.objects.filter(user=request.user.id)
        cursos = Curso.objects.all()
        return render(request, "cursos.html", {"cursos":cursos,"url":avatares[0].imagen.url})
    else:
        return render(request, "cursos.html")
    # dicc = {"cursos":cursos}
    # plantillas = loader.get_template("cursos.html")
    # documento = plantillas.render(dicc)
    # return HttpResponse(documento)

def alta_curso(request, nombre , comision):
    curso = Curso(nombre=nombre , comision=comision)
    curso.save()
    texto = f"Se guardo en el BD el Curso: {curso.nombre} Comision:{curso.comision}"
    return HttpResponse(texto)

def alta_alumno(request, nombre , apellido):
    alumno = Alumnos(nombre=nombre , apellido=apellido)
    alumno.save()
    texto = f"Se guardo en el BD el Alumno: {alumno.nombre} Apellido:{alumno.apellido}"
    return HttpResponse(texto)

def alta_profesor(request, nombre , apellido):
    profesor = Profesores(nombre=nombre , apellido=apellido)
    profesor.save()
    texto = f"Se guardo en el BD el Profesor: {profesor.nombre} Apellido:{profesor.apellido}"
    return HttpResponse(texto)

@login_required
def profesores(request):
    print(request.user.id)
    if request.user.id != None:
        avatares = Avatar.objects.filter(user=request.user.id)
        profesores = Profesores.objects.all()
        return render(request, "profesores.html", {"profesores":profesores,"url":avatares[0].imagen.url})

def alumnos(request):
    print(request.user.id)
    if request.user.id != None:
        avatares = Avatar.objects.filter(user=request.user.id)
        alumnos = Alumnos.objects.all
        return render( request , "alumnos.html", {"alumnos":alumnos,"url":avatares[0].imagen.url})
    else:
        return render( request , "alumnos.html")


def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_form( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos['nombre'] , comision=datos['comision'])
            curso.save()
            return render( request , "formulario.html")
    
    return render( request , "formulario.html")

def alumno_formulario(request):

    if request.method == "POST":

        mi_formulario2 = Alumnos_form( request.POST )

        if mi_formulario2.is_valid():
            datos2 = mi_formulario2.cleaned_data
            alumno = Alumnos( nombre=datos2['nombre'] , apellido=datos2['apellido'])
            alumno.save()
            return render( request , "formulario2.html") 
        
    return render( request , "formulario2.html")

def profesor_formulario(request):

    if request.method == "POST":

        mi_formulario3 = Profesores_form( request.POST )

        if mi_formulario3.is_valid():
            datos3 = mi_formulario3.cleaned_data
            profesor = Profesores( nombre=datos3['nombre'] , apellido=datos3['apellido'])
            profesor.save()
            return render( request , "formulario3.html") 
        
    return render( request , "formulario3.html")

def buscar_curso(request):
    return render( request , "buscar_curso.html")

def buscar_alumno(request):
    return render( request , "buscar_alumno.html")

def buscar_profesor(request):
    return render( request , "buscar_profesor.html")

def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request, "resultado_busqueda.html", {"cursos": cursos})
    else:
        return HttpResponse("Campo vacio")
    
def buscar2(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        alumnos = Alumnos.objects.filter(nombre__icontains = nombre)
        return render( request, "resultado_busqueda2.html", {"alumnos": alumnos})
    else:
        return HttpResponse("Campo vacio")
    
def buscar3(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        profesores = Profesores.objects.filter(nombre__icontains = nombre)
        return render( request, "resultado_busqueda3.html", {"profesores": profesores})
    else:
        return HttpResponse("Campo vacio")
    
def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    curso=Curso.objects.all()
    return render(request, "cursos.html", {"cursos": cursos})

def eliminar_alumno(request, id):
    alumno = Alumnos.objects.get(id=id)
    alumno.delete()
    alumno=Alumnos.objects.all()
    return render(request, "alumnos.html", {"alumnos": alumnos})

def eliminar_profesor(request, id):
    profesor = Profesores.objects.get(id=id)
    profesor.delete()
    profesor=Profesores.objects.all()
    return render(request, "profesores.html", {"profesores": profesores})

def editar( request , id):

    curso = Curso.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Curso_form( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos['nombre']
            curso.comision = datos['comision']
            curso.save()

            curso = Curso.objects.all()          
            return render(request , "cursos.html" , {"cursos": cursos})
    else:
        mi_formulario = Curso_form(initial={'nombre':curso.nombre , "comision":curso.comision})
    
    return render( request , "editar_curso.html" , {"mi_formulario":mi_formulario, "curso": curso})


def editar_alumno( request , id):

    alumno = Alumnos.objects.get(id=id)

    if request.method == "POST":

        mi_formulario2 = Alumnos_form( request.POST )
        if mi_formulario2.is_valid():
            datos2 = mi_formulario2.cleaned_data
            alumno.nombre = datos2['nombre']
            alumno.apellido = datos2['apellido']
            alumno.save()

            alumno = Alumnos.objects.all()          
            return render(request , "alumnos.html" , {"alumnos": alumnos})
    else:
        mi_formulario2 = Alumnos_form(initial={'nombre':alumno.nombre , "apellido":alumno.apellido})
    
    return render( request , "editar_alumno.html" , {"mi_formulario2":mi_formulario2, "alumno": alumno})

def editar_profesor( request , id):

    profesor = Profesores.objects.get(id=id)

    if request.method == "POST":

        mi_formulario3 = Profesores_form( request.POST )
        if mi_formulario3.is_valid():
            datos3 = mi_formulario3.cleaned_data
            profesor.nombre = datos3['nombre']
            profesor.apellido = datos3['apellido']
            profesor.save()

            profesor = Profesores.objects.all()          
            return render(request , "profesores.html" , {"profesores": profesores})
    else:
        mi_formulario3 = Profesores_form(initial={'nombre':profesor.nombre , "apellido":profesor.apellido})
    
    return render( request , "editar_profesor.html" , {"mi_formulario3":mi_formulario3, "profesor": profesor})


def login_request(request):
    if request.method == "POST":

        form = AuthenticationForm(request , data=request.POST)

        if form.is_valid(): 
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username , password=password)

            if user is not None:
                login(request , user)
                avatares = Avatar.objects.filter(user=request.user.id)
                return render(request, "inicio.html", {"mensaje":f"Bienvenido/a: {username}", "url":avatares[0].imagen.url})
            else:
                return HttpResponse(f"Usuario Incorrecto")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")          

    form = AuthenticationForm()
    return render(request, "login.html", {"form":form})


def logout_request(request):
    return render(request, "logout.html")

def register(request):
    if request.method == "POST":
        pass 

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Usuario Creado")

        else:
            form = UserCreationForm()

        return render(request, "register.html", {"form":form})


@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            password1 = informacion['password1']
            usuario.set_password(password1)
            usuario.save()

            return render(request, "inicio.html")

    

    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render(request, "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})
