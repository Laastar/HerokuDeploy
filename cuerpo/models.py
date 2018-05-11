from django.db import models
from django.utils import timezone
from .choices import *
from django.contrib import messages, sessions

# Create your models here. Va

class Post(models.Model):
    """
    Modelo para almacenar los posts
    """
    autor = models.ForeignKey('auth.User', on_delete= models.CASCADE)
    titulo = models.CharField(max_length= 200)
    texto = models.TextField()
    fechaCreacion = models.DateTimeField(
        default = timezone.now
    )
    fechaPublicacion = models.DateTimeField(
        blank= True, null = True
    )

    def publicar(self):
        """
        Método para obtener la fecha de publicación
        cuando se publique algún Post
        """
        self.fechaPublicacion = timezone.now()
        self.save()

    #Método mágico que nos permite castear un objeto a una cadena
    def __str__(self):
        return self.titulo


class User(models.Model):
    username = models.CharField(max_length=30, help_text='Nombre de usuario', primary_key=True)
    password1 = models.CharField(max_length=30, help_text='Contraseña')
    password2 = models.CharField(max_length=30, help_text='Confirmacion de contraseña')
    first_name = models.CharField(max_length=30, help_text='Nombre')
    last_name = models.CharField(max_length=30, help_text='Apellido')
    email = models.EmailField(max_length=254, help_text='Correo electronico')

    def __str__(self):
        return self.username


class Logeado(models.Model):
    username = models.CharField(max_length=30, help_text='Nombre de usuario')
    password = models.CharField(max_length=30, help_text='Contraseña')

    def __str__(self):
        return self.username

class Recuperacion(models.Model):
    email = models.EmailField(max_length=254, help_text='Correo electronico')

    def __str__(self):
        return self.email

#username = request.session.get('USUARIO_LOGEADO')

class HacerCita(models.Model):
    username = models.CharField(max_length=30, help_text='Nombre de usuario')
    hora = models.TimeField(help_text="Formato hora:minutos")
    dia = models.DateField(help_text="Formato dia/mes/año")
    email = models.EmailField(help_text='Correo electronico')
    servicio = models.CharField(max_length=25, choices=SERVICES_CHOICES2, help_text='Eliga su servicio', default='1')

class Opiniones(models.Model):
    texto = models.CharField(max_length=300, default="")
    terminos = models.BooleanField(default=True)

    def __str__(self):
        return self.texto

class Producto(models.Model):
    id = models.AutoField
    nombre = models.CharField(max_length=120)
    precio = models.DecimalField(decimal_places=3, max_digits=10)
    descricpion = models.CharField(max_length=300, default="")
    imagen = models.CharField(max_length=120)
    nota = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre

class Barnice(models.Model):
    id = models.AutoField
    nombre = models.CharField(max_length=120)
    precio = models.DecimalField(decimal_places=3, max_digits=10)
    descricpion = models.CharField(max_length=300, default="")
    imagen = models.CharField(max_length=120)
    nota = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre

class CuidadoPersonal(models.Model):
    id = models.AutoField
    nombre = models.CharField(max_length=120)
    precio = models.DecimalField(decimal_places=3, max_digits=10)
    descricpion = models.CharField(max_length=300, default="")
    imagen = models.CharField(max_length=120)
    nota = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre

class CuidadoCabello(models.Model):
    id = models.AutoField
    nombre = models.CharField(max_length=120)
    precio = models.DecimalField(decimal_places=3, max_digits=10)
    descricpion = models.CharField(max_length=300, default="")
    imagen = models.CharField(max_length=120)
    nota = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre

class PerfumesLociones(models.Model):
    id = models.AutoField
    nombre = models.CharField(max_length=120)
    precio = models.DecimalField(decimal_places=3, max_digits=10)
    descricpion = models.CharField(max_length=300, default="")
    imagen = models.CharField(max_length=120)
    nota = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre

