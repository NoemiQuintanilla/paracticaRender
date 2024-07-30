from django.db import models

# Creando modelo de de genero: terror ,
class Genero (models.Model):
    id=models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=25)
    descripcion = models.CharField(max_length=150,default='')
    # cargar archivo
    foto=models.FileField(upload_to='generos', null=True, blank=True)
    # personalizar la vista del admin
    def __str__(self):
        fila= "{0}: {1}-{2}"
        return fila.format(self.id,self.nombre,self.descripcion)

# creando el modelo de director

class Director (models.Model):
    id= models.AutoField(primary_key=True)
    dni = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fotografia=models.FileField(upload_to='fotografias', null=True, blank=True)
    estado=models.BooleanField(default=True)
    # personalizar la vista en el admin 
    def __str__(self):
        fila= "{0}: {1}  -  {2}  -  {3}  -  {4}"
        return fila.format(self.id,self.dni,self.nombre,self.apellido, self.estado)

# creando el modelo pais

class Pais (models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    continente = models.CharField(max_length=20)
    capital = models.CharField(max_length=50)
    
    def __str__(self):
        fila= "{0}: {1}  -  {2}  -  {3} "
        return fila.format(self.id,self.nombre,self.capital,self.continente)
    
# clase de pelicula
class Pelicula(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=250)
    duracion=models.TimeField(null=True)
    sinopsis= models.TextField()
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    director = models.ForeignKey(Director,on_delete=models.CASCADE)
    pais= models.ForeignKey(Pais,on_delete=models.CASCADE)

    # METODO DE VISUALIZACION
    def __str__(self):
        fila="{0}: {1}"
        return fila.format(self.id,self.titulo)
    
class Cine(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=250)
    direccion=models.CharField(max_length=250)
    telefono=models.CharField(max_length=250)
# METODO DE VISUALIZACION
    def __str__(self):
        fila="{0}: {1}"
        return fila.format(self.id,self.nombre)
    
    