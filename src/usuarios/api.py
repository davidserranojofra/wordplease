from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from usuarios.serializers import UsuarioSerializer




#API Listado de blogs
class ListarblogsAPI(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UsuarioSerializer





class ListarActualizarBorrarUsuarios(RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UsuarioSerializer