from rest_framework import serializers
from django.contrib.auth.models import User
from usuarios.models import ProfileUsuario


class UsuarioRegistroSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
            username=validated_data.get('username')
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user



class ListadoBlogsUsuariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username']



class PostDetalleSerializer(serializers.ModelSerializer):

    class Meta:
      model = User
      fields = '__all__'



class ProfileUsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileUsuario
        fields = '__all__'