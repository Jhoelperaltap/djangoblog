from django.urls import path
from.views import *

urlpatterns = [
    path('', home, name='index'),
    path('generales/', generales, name = 'generales'),
    path('tecnologia/', tecnologia, name = 'tecnologia'),
    path('programacion/', programacion, name = 'programacion'),
    path('tutoriales/', tutoriales, name = 'tutoriales'),
    path('videojuegos/', videojuegos, name = 'videojuegos'),
    path('detallePost/<slug:slug>/', detallePost, name ='detallePost'),
         
]

