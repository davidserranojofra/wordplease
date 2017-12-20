from django.contrib.auth.models import User
from rest_framework import serializers



class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
      Model = User
      fields = '__all__'


