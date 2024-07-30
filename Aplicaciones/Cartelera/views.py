from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render

from Aplicaciones.Cartelera.models import Cine, Genero,Pelicula,Director,Pais
# importar libreria de mensajes de python 
from django.contrib import messages



# Create your views here.

def home(request):
    return render (request,"home.html")



# renderizar el template genero
def listadoGeneros(request):
    generosBdd=Genero.objects.all()
    return render(request,"listadoGeneros.html",{'generos':generosBdd})


# renderizar Peliculas 
def listadoPeliculas(request):
    peliculasbdd=Pelicula.objects.all()
    return render(request,"ListadoPeliculas.html",{'peliculas':peliculasbdd})
# renderizar directores
def listadoDirector(request):
    directoresdbb= Director.objects.all()
    return render(request,"listadoDirector.html",{'directores':directoresdbb})
# renderizar pais
def listadoPais(request):
    paisbdd= Pais.objects.all()
    return render(request,"listadoPais.html",{'paises':paisbdd})

# boton eliminar
def eliminarGenero(request,id):
    generoEliminar=Genero.objects.get(id=id)
    generoEliminar.delete()
    messages.success(request,"Genero Eliminado")
    return redirect('listadoGeneros')


# renderizando del nuevo genero 
def nuevoGenero(request):
    return render(request,'nuevoGenero.html')


# renderizando guardar GENERO 
def guardarGenero(request):
    nom=request.POST["nombre"]
    des=request.POST["descripcion"]
    fot=request.FILES.get("foto")
    newGenero=Genero.objects.create(nombre=nom,descripcion=des, foto=fot)
    # aqui van los mensajes
    messages.success(request,"Género registrado")
    
    return redirect('listadoGeneros')

# renderizando formulario de editar
def editarGenero(request,id):
    generoEditar=Genero.objects.get(id=id)
    return render(request, 'editarGenero.html',{'generoEditar':generoEditar})

# actualizar los nuevos datos en la BDD
def procesarActualizacionGenero(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    generoConsultado=Genero.objects.get(id=id)
    generoConsultado.nombre=nombre
    generoConsultado.descripcion=descripcion
    generoConsultado.save()
    messages.success(request,'Datos actualizados')
    return redirect('listadoGeneros')

# crud para pais
# renderizando del nuevo pais 
def nuevoPais(request):
    return render(request,'nuevoPais.html')
def guardarPais(request):
    nombre = request.POST['nombre']
    continente = request.POST['continente']
    capital = request.POST['capital']
    newGenero=Pais.objects.create(nombre=nombre,continente=continente,capital=capital)
    # aqui van los mensajes
    messages.success(request,"Nuevo Pais registrado")
    
    return redirect('listadoPais')

# eliminar pais 
def eliminarPais(request,id):
    paisEliminar=Pais.objects.get(id=id)
    paisEliminar.delete()
    messages.success(request,"Pais Eliminado")
    return redirect('listadoPais')
# renderizar la vista de editar pais
def editarPais(request,id):
    paisEditar=Pais.objects.get(id=id)
    return render(request, 'editarPais.html',{'paisEditar':paisEditar})

# ejecutar la actualizacion 
def procesarActualizacionPais(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    continente = request.POST['continente']
    capital = request.POST['capital']
    paisConsultado=Pais.objects.get(id=id)
    paisConsultado.nombre=nombre
    paisConsultado.continente=continente
    paisConsultado.capital=capital
    paisConsultado.save()
    messages.success(request,'Datos actualizados')
    return redirect('listadoPais')    

#crud para Director
#renderizando del nuevo director 
def nuevoDirector(request):
    return render(request,'nuevoDirector.html')

def guardarDirector(request):
    dni=request.POST['cedula']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    fot=request.FILES.get("fotografia")
    newGenero=Director.objects.create(dni=dni,nombre=nombre,apellido=apellido, fotografia=fot)
    # aqui van los mensajes
    messages.success(request,"Nuevo Director registrado")
    
    return redirect('listadoDirector')
def eliminarDirector(request,id):
    directorEliminar=Director.objects.get(id=id)
    directorEliminar.delete()
    messages.success(request,"Director Eliminado")
    return redirect('listadoDirector')
# renderizar la vista de editar Director
def editarDirector(request,id):
    directorEditar=Director.objects.get(id=id)
    return render(request, 'editarDirector.html',{'directorEditar':directorEditar})

# ejecutar la actualizacion 
def procesarActualizacionDirector(request):
    id = request.POST['id']
    dni = request.POST['cedula']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    directorConsultado=Director.objects.get(id=id)
    directorConsultado.nombre=nombre
    directorConsultado.apellido=apellido
    directorConsultado.dni=dni
    directorConsultado.save()
    messages.success(request,'Datos actualizados')
    return redirect('listadoDirector')    

def gestionCines(request):
    return render(request,'gestionCines.html')


# usando ajax 
@csrf_exempt
def guardarCine (request):
    nombre = request.POST['nombre']
    dir = request.POST['direccion']
    tel = request.POST['telefono']
    nuevoCine = Cine.objects.create(nombre=nombre,direccion=dir, telefono=tel)
    return JsonResponse ({
        'estado':True,
        'mensaje':'Cine Registrado Exitosamente',    
    })

def listadoCines(request):
    cinebdd= Cine.objects.all()
    return render(request,"listadoCines.html",{'cines':cinebdd})


# renderizar la vista 
def gestionarDirector(request):
    return render(request,'Director/gestionarDirector.html')
# usando fetch
@csrf_exempt
def agregarDirector(request):
    dni=request.POST['dni']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    fot=request.FILES.get("fotografia")
    estado = request.POST.get("estado") == 'on'
    
    newGenero=Director.objects.create(dni=dni,nombre=nombre,apellido=apellido, fotografia=fot, estado=estado)

    return JsonResponse ({
        'estado':True,
        'mensaje':'Director Registrado Exitosamente',    
    })

def listadoDirectores(request):
    directoresBdd= Director.objects.all()
    return render(request,"Director/listadoDirectores.html",{'directores':directoresBdd})


# usando flech para peliculas
def gestionarPeliculas(request):
    generosBdd = Genero.objects.all()
    directoreBdd = Director.objects.all()
    paisesBdd = Pais.objects.all()
    return render(request,'Peliculas/gestionarPeliculas.html',{'generos':generosBdd,'directores':directoreBdd,'paises':paisesBdd})


def agregarPelicula(request):
    titulo = request.POST["titulo"]
    duracion = request.POST["duracion"]
    sinopsis = request.POST["sinopsis"]
    genero_id = request.POST["genero"]
    director_id = request.POST["director"]
    pais_id = request.POST["pais"]


    # Obtener instancias de Genero y Director
    genero = Genero.objects.get(id=genero_id)
    director = Director.objects.get(id=director_id)
    pais =Pais.objects.get(id=pais_id)

    nuevaPelicula = Pelicula.objects.create(titulo=titulo,duracion=duracion,sinopsis=sinopsis,genero=genero,director=director,pais=pais)

    generos = Genero.objects.all()
    directores = Director.objects.all()
    paises = Pais.objects.all()
    return JsonResponse({
        'estado': True,
        'mensaje': 'Pelicula registrada exitosamente',
    })
    
    # Listar Peliculas
def listadoPeliculas(request):
    peliculasBdd =  Pelicula.objects.all()
    return render(request,'Peliculas/listadoPeliculas.html',{'peliculas':peliculasBdd})


# def exportCinesPDF(request):
#     #llamar a todos los datos del modelo cina
#     cines = Cine.objects.all()
#     #llamar al template con el render string
#     html_string = render_to_string('exportCines.html', {'cines': cines})
#     #almacenar como un archivo html
#     html = HTML(string=html_string)
#     #leer todo el html guardado y convvertirlo en un pdf
#     pdf = html.write_pdf()
#     #dar una respuesta como pdf(archivo)
#     response = HttpResponse(pdf, content_type='application/pdf')
#     #nombrar y dar una extension al archivo expotado
#     response['Content-Disposition'] = 'attachment; filename="reporte_cines.pdf"'
#     #exportar archivo
#     return response
