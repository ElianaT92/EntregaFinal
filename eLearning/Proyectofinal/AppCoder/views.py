from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
from AppCoder.models import Profesores
from AppCoder.models import Egresados
from django.core import serializers
from AppCoder.forms import CursoFormulario
from AppCoder.forms import ProfesorFormulario
from AppCoder.forms import EgresadosFormulario

# Create your views here.
def cursos(request):

    if request.method == "POST":
	    
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                curso = Curso(nombre=informacion["curso"], inicio=informacion["inicio"], duracion=informacion['duracion'], costo=informacion['costo'])
                curso.save()
                return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario()	
    
    return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})

def profesores(request):

    if request.method == "POST":
	    
            profeFormulario = ProfesorFormulario(request.POST) # Aqui me llega la informacion del html
            print(profeFormulario)

            if profeFormulario.is_valid:
                resultado = profeFormulario.cleaned_data
                profesores = Profesores(profesor=resultado["profesor"], asignatura=resultado["asignatura"],cargo=resultado['cargo'], actividad=resultado['actividad'])
                profesores.save()
                return render(request, "AppCoder/inicio.html")
    else:
        profeFormulario = ProfesorFormulario()	
    
    return render(request, "AppCoder/profesores.html", {"profeFormulario": profeFormulario})

def egresados(request):

    if request.method == "POST":
	    
            egresoFormulario = EgresadosFormulario(request.POST) # Aqui me llega la informacion del html
            print(egresoFormulario)

            if egresoFormulario.is_valid:
                resultadoegresados = egresoFormulario.cleaned_data
                egresados = Egresados(nombre=resultadoegresados["egresado"], titulacion=resultadoegresados["titulacion"], graduacion=resultadoegresados['graduacion'], promedio=resultadoegresados['egresados'])
                egresados.save()
                return render(request, "AppCoder/inicio.html")
    else:
        egresoFormulario = EgresadosFormulario()	
    
    return render(request, "AppCoder/egresados.html", {"egresoFormulario": egresoFormulario})

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursosapi(request):
    cursos_todos=Curso.objects.all()
    return HttpResponse (serializers.serialize('json',cursos_todos))

def profesoresapi(request):
    profesores_todos=Profesores.objects.all()
    return HttpResponse (serializers.serialize('json',profesores_todos))

def buscarcurso(request):
    return render(request, 'AppCoder/busquedaCurso.html')

def buscar(request):
    inicio_views= request.GET['inicio']
    cursos_todos=Curso.objects.filter(inicio=inicio_views)
    return render(request, 'AppCoder/resultadoCurso.html',{'inicio':inicio_views,'cursos':cursos_todos})

def buscarprofesor(request):
    return render(request, 'AppCoder/busquedaProfesor.html')

def buscarprofe(request):
    asignatura_views= request.GET['asignatura']
    profesores_todos=Profesores.objects.filter(asignatura=asignatura_views)
    return render(request, 'AppCoder/resultadoProfesor.html',{'asignatura':asignatura_views,'profesores':profesores_todos})

def buscaregreso(request):
    titulacion_views= request.GET['titulacion']
    egresados_todos=Egresados.objects.filter(titulacion=titulacion_views)
    return render(request, 'AppCoder/resultadoEgresado.html',{'titulacion':titulacion_views,'egresados':egresados_todos})

def buscaregresado(request):
    return render(request, 'AppCoder/busquedaEgresado.html')

def leer_curso(request):
    cursos_all=Curso.objects.all()
    return HttpResponse(serializers.serialize('json', cursos_all))

def crear_curso(request):
    curso= Curso(nombre='CursoTest', camada= 201)
    curso.save()
    return HttpResponse(f'Curso {curso.nombre} ha sido creado')

def editar_curso(request):
    nombre_consulta= 'CursoTest'
    Curso.objects.filter(nombre=nombre_consulta).update(nombre='nombrenuevoCursoTest')
    return HttpResponse (f'Curso {nombre_consulta} ha sido actualizado')

def eliminar_curso(request):
    nombre_nuevo= 'nombrenuevoCursoTest'
    curso=Curso.objects.get(nombre=nombre_nuevo)
    curso.delete()
    return HttpResponse (f'Curso {nombre_nuevo} ha sido eliminado')

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class CursoList(ListView):
    model= Curso
    template= 'AppCoder/curso_list.html'


class CursoCreate(CreateView):
    model= Curso
    fields= '__all__'
    success_url='/AppCoder/curso/list/'


class CursoEdit(UpdateView):
    model= Curso
    fields= '__all__'
    success_url='/AppCoder/curso/list/'

from django.views.generic.detail import DetailView

class CursoDetail(DetailView):
    model= Curso
    template_name= 'AppCoder/curso_detail.html'

class CursoDelete(DeleteView):
    model=Curso
    success_url= '/AppCoder/curso/list'

class ProfeList(ListView):
    model= Profesores
    template= 'AppCoder/profesores_list.html'

class ProfeCreate(CreateView):
    model=Profesores
    fields= '__all__'
    success_url='/AppCoder/profesores/list/'

class ProfeDetail(DetailView):
    model= Profesores
    template_name= 'AppCoder/profesores_detail.html'

class ProfeDelete(DeleteView):
    model=Profesores
    success_url= '/AppCoder/profesores/list'

class ProfeEdit(UpdateView):
    model= Profesores
    fields= '__all__'
    success_url='/AppCoder/profesores/list/'

#EGRESADOS
class EgresoList(ListView):
    model= Egresados
    template= 'AppCoder/egresados_list.html'

class EgresoCreate(CreateView):
    model= Egresados
    fields= '__all__'
    success_url='/AppCoder/egresados/list/'

class EgresoDetail(DetailView):
    model= Egresados
    template_name= 'AppCoder/egresados_detail.html'

class EgresoDelete(DeleteView):
    model=Egresados
    success_url= '/AppCoder/egresados/list'

class EgresoEdit(UpdateView):
    model= Egresados
    fields= '__all__'
    success_url='/AppCoder/egresados/list/'





