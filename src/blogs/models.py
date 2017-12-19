from django.contrib.auth.models import User
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descricion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Post(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    titulo = models.CharField(max_length=50)
    resumen = models.TextField()
    cuerpo_del_post = models.TextField()
    url_foto = models.URLField()
    categoria = models.ManyToManyField(Categoria)
    fecha_publicacion = models.DateTimeField()

    creado_en = models.DateTimeField(auto_now_add=True)
    modificado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo