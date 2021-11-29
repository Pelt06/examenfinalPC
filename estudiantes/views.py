from django.shortcuts import render, get_object_or_404

from django.contrib import messages
from .forms import CursoForm
from estudiantes.models import Asignacion, Estudiante, Curso

def list_Cursos(request):
    posts = Curso.objects.all()
    return render(request, 'estudiantes/listado_cursos.html', {'cursos': posts})

def detalle_Cursos(request, curso_id):
    curso= Curso.objects.get(pk=curso_id)
    return render(request, 'estudiantes/detalle_curso.html',{'curso': curso} )

def nuevo_curso(request):
    if request.method == "POST":
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            curso = Curso.objects.create(nombre=formulario.cleaned_data['nombre'], seccion = formulario.cleaned_data['seccion'])
            for estudiante_id in request.POST.getlist('actores'):
                asignacion = Asignacion(estudiante_id=estudiante_id, curso_id = curso.id)
                asignacion.save()
            messages.add_message(request, messages.SUCCESS, 'Curso Guardado Exitosamente')
    else:
        formulario = CursoForm()
    return render(request, 'estudiantes/editar_curso.html', {'formulario': formulario})

