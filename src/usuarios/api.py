from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from usuarios.permissions import UsuariosPermisos
from usuarios.serializers import PostDetalleSerializer, UsuarioRegistroSerializer, ListadoBlogsUsuariosSerializer


# API Listado de blogs --->

class ListadoBlogsUsuarios(ListAPIView):

    queryset = User.objects.all()
    serializer_class = ListadoBlogsUsuariosSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['username']
    ordering_fields = ['first_name', 'last_name']



# API de usuarios --->

class RegistroUsuario(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UsuarioRegistroSerializer


class UsuarioDetalleAPI(RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = PostDetalleSerializer
    permission_classes = [UsuariosPermisos]