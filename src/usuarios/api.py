from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from usuarios.models import Profile
from usuarios.permissions import UsuariosPermisos
from usuarios.serializers import PostDetalleSerializer, UsuarioRegistroSerializer, ListadoBlogsUsuariosSerializer, \
    ProfileSerializer


# API Listado de blogs --->

class ListadoBlogsUsuarios(ListAPIView):
    queryset = User.objects.all()
    serializer_class = ListadoBlogsUsuariosSerializer
    permission_classes = [AllowAny]
    search_fields = ['username']
    ordering_fields = ['first_name']


# API de usuarios --->

class RegistroUsuario(CreateAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UsuarioDetalleAPI(RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = PostDetalleSerializer
    permission_classes = [UsuariosPermisos]