from rest_framework import serializers
from django.contrib.auth.models import User



class UsuarioRegistroSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

     #   def create(self, validated_data):
     #       user = User(
     #           first_name=validated_data['first_name'],
     #           last_name=validated_data['last_name'],
     #           email=validated_data['email'],
     #           username=validated_data['username']
     #       )
     #       user.set_password(validated_data['password'])
     #       user.save()
     #       return user

        def restore_object(self, attrs, instance=None):
            user = super(UsuarioRegistroSerializer, self).restore_object(attrs, instance)
            user.set_password(attrs['password'])
            return user

class ListadoBlogsUsuariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username']


#class UsuarioSerializer(serializers.ModelSerializer):
#
#    class Meta:
#      model = User
#      fields = ['id', 'titulo', 'url_foto', 'resumen', 'fecha_de_publicacion']


class PostDetalleSerializer(serializers.ModelSerializer):

    class Meta:
      model = User
      fields = '__all__'

