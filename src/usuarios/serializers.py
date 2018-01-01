from rest_framework import serializers
from django.contrib.auth.models import User


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


class ProfileSerializer(UsuarioRegistroSerializer):
    #usuario = UsuarioRegistroSerializer(read_only=True)

    class Meta:
        model = User
        fields = '__all__'



class ListadoBlogsUsuariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username']



class PostDetalleSerializer(serializers.ModelSerializer):

    class Meta:
      model = User
      fields = '__all__'



class UsuarioMostrarSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']



