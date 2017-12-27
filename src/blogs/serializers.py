from rest_framework import serializers
from blogs.models import Post



class PostSerializer(serializers.ModelSerializer):

    class Meta:
      model = Post
      fields = ['id', 'titulo', 'url_foto', 'resumen', 'fecha_publicacion']


class PostDetalleSerializer(serializers.ModelSerializer):

    #usuario = UsuarioRegistroSerializer(read_only=True)

    class Meta:
      model = Post
      fields = '__all__'
      read_only_fields = ['usuario']


class PublicarPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['usuario']