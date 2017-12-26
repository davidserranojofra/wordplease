from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView

from usuarios.permissions import UsuariosPermisos
from usuarios.serializers import PostDetalleSerializer, UsuarioRegistroSerializer, ListadoBlogsUsuariosSerializer


# API Listado de blogs --->

class ListadoBlogsUsuarios(ListAPIView):
    queryset = User.objects.all()
    serializer_class = ListadoBlogsUsuariosSerializer
    search_fields = ['username']
    ordering_fields = ['first_name']


# API de usuarios --->

class RegistroUsuario(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UsuarioRegistroSerializer


class UsuarioDetalleAPI(RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = PostDetalleSerializer
    permission_classes = [UsuariosPermisos]