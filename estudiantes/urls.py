from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #url('', views.lista_peliculas, name ='lista_peliculas'),
    url('cursos/', views.list_Cursos, name='listado_cursos'),
    path('curso/<curso_id>/', views.detalle_Cursos, name='detalle_curso'),
    url('nuevo/curso/', views.nuevo_curso, name='nuevo_curso'),
    ]