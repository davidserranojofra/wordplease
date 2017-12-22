from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError



class UsuarioListaSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    username = serializers.CharField()


class UsuarioSerializer(UsuarioListaSerializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_username(self, data):
        if self.instance is None and User.objects.filter(username=data).exists():
            raise ValidationError('Este usuario ya existe')
        if self.instance is not None and self.instance.username != data and User.objects.filter(username=data).exists():
            raise ValidationError('El usuario ya esta en uso')
        return data

    def create(self, validate_data):
        instance = User()
        return self.update(instance, validate_data)

    def update(self, instance, validate_data):
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance

