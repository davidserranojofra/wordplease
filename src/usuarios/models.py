from django.db import models


class Post(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=50)
    email = models.EmailField()
    contrasenya = models.CharField(max_length=25)