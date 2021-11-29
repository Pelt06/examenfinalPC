from django.db import models
from django.contrib import admin

class Estudiante(models.Model):
    carnet  =   models.CharField(max_length=30)
    nombre  =   models.CharField(max_length=30)
    apellido  =   models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre    = models.CharField(max_length=60)
    seccion      = models.CharField(max_length=1)
    actores   = models.ManyToManyField(Estudiante, through='Asignacion')

    def __str__(self):
        return self.nombre

class Asignacion (models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)


class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1


class EstudianteAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)

class CursoAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)