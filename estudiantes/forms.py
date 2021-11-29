from django import forms
from .models import Estudiante, Curso


class CursoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Curso
        fields = ('nombre', 'seccion', 'actores')

    def __init__ (self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)
        self.fields["actores"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["actores"].help_text = "Ingrese los estudiantes asignados al curso"
        self.fields["actores"].queryset = Estudiante.objects.all()