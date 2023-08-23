from django.http import HttpResponse
from django.template import Template,Context,loader


def test_template(request):
    datos = {"Nombre":"Pepe", "Notas":[10,9,8,7,6,5,4,3,2,1]}
    plantilla = loader.get_template("template.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)



"""
def test_template(request):
   
    mi_html = open("C:/Users/juan.buenanueva/OneDrive - Accenture/Desktop/Cursos/CoderHouse/Python/Coder-56650/Clase 18/Proyecto1/Proyecto1/plantillas/template.html")

    plantilla = Template( mi_html.read() )

    mi_html.close()

    mi_contexto = Context({"Nombre":"Pepe", "Notas":[10,9,8,7,6,5,4,3,2,1]})

    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)
"""