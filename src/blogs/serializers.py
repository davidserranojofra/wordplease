from rest_framework import serializers
from blogs.models import Post
from usuarios.serializers import UsuarioMostrarSerializer


class PostSerializer(serializers.ModelSerializer):

    class Meta:
      model = Post
      fields = ['id', 'titulo', 'url_foto', 'resumen', 'fecha_publicacion']


class PostDetalleSerializer(serializers.ModelSerializer):

    usuario = UsuarioMostrarSerializer(read_only=True)

    class Meta:
      model = Post
      fields = '__all__'
      read_only_fields = ['usuario']


class PublicarPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['usuario']