from django.shortcuts import render
from AppCoder.models import Curso
from django.template import loader
from django.http import HttpResponse
from AppCoder.forms import Curso_form
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.

def inicio(request):
    return render( request , "padre.html")

def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos":cursos}
    plantillas = loader.get_template("cursos.html")
    documento = plantillas.render(dicc)
    return HttpResponse(documento)

def alta_curso(request, nombre , comision):
    curso = Curso(nombre=nombre , comision=comision)
    curso.save()
    texto = f"Se guardo en el BD el Curso: {curso.nombre} Comision:{curso.comision}"
    return HttpResponse(texto)

def profesores(request):
    return render( request , "profesores.html")

def alumnos(request):
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

def buscar_curso(request):
    return render( request , "buscar_curso.html")

def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request, "resultado_busqueda.html", {"cursos": cursos})
    else:
        return HttpResponse("Campo vacio")
    
def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    curso=Curso.objects.all()
    return render(request, "cursos.html", {"cursos": cursos})

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

def login_request(request):
    if request.method == "POST":

        form = AuthenticationForm(request , data=request.POST)

        if form.is_valid(): 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username , password=password)

            if user is not None:
                login(request , user)
                return render(request, "inicio.html", {"mensaje":f"Bienvenido {username}"})
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


