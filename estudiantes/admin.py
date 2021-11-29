from django.contrib import admin
from .models import Estudiante, EstudianteAdmin, Curso, CursoAdmin

# Register your models here.

admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Curso, CursoAdmin)