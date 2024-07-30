from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('listadoGeneros/',views.listadoGeneros, name='listadoGeneros'),
    path('listadoPeliculas/',views.listadoPeliculas,name='listadoPeliculas'),
    path('listadoDirector/',views.listadoDirector,name='listadoDirector'),
    path('listadoPais/',views.listadoPais, name='listadoPais'),
    path('eliminarGenero/<id>',views.eliminarGenero, name='eliminarGenero'),
    path('nuevoGenero/',views.nuevoGenero,name='nuevoGenero'),
    path('guardarGenero/',views.guardarGenero,name='guardarGenero'),
    path('editarGenero/<id>',views.editarGenero,name='editarGenero'),
    path('procesarActualizacionGenero/',views.procesarActualizacionGenero,name='procesarActualizacionGenero'),
    path('nuevoPais',views.nuevoPais,name='nuevoPais'),
    path('guardarPais/',views.guardarPais,name='guardarPais'),
    path('eliminarPais/<id>',views.eliminarPais, name='eliminarPais'),
    path('editarPais/<id>',views.editarPais,name='editarPais'),
    path('procesarActualizacionPais/',views.procesarActualizacionPais,name='procesarActualizacionPais'),
    path('nuevoDirector',views.nuevoDirector,name='nuevoDirector'),
    path('eliminarDirector/<id>',views.eliminarDirector, name='eliminarDirector'),
    path('guardarDirector/',views.guardarDirector,name='guardarDirector'),
    path('editarDirector/<id>',views.editarDirector,name='editarDirector'),
    path('procesarActualizacionDirector/',views.procesarActualizacionDirector,name='procesarActualizacionDirector'),
    path('gestionCines/',views.gestionCines,name='gestionCines'),
    path('guardarCine/',views.guardarCine,name='guardarCine'),
    path('listadoCines/',views.listadoCines,name='listadoCines'),
    # usando fetch 
    path('gestionarDirector/',views.gestionarDirector,name='gestionarDirector'),
    path('agregarDirector/',views.agregarDirector,name='agregarDirector'),
    path('listadoDirectores/',views.listadoDirectores,name='listadoDirectores'),
    # usando fetch para peliculas
    path('gestionarPeliculas/',views.gestionarPeliculas,name='gestionarPeliculas'),
    path('agregarPeliculas/',views.agregarPelicula,name='agregarPeliculas'),
    path('listadoPeliculas/',views.listadoPeliculas,name='listadoPeliculas'),
    


    
]