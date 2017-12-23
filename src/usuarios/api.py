from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

#from usuarios.serializers import UsuarioSerializer, UsuarioListaSerializer


#Listado y creacion de usuarios

#class UsuariosListaAPI(APIView):
#    def get(self, request):
#        usuarios = User.objects.all()
#        serializer = UsuarioListaSerializer(usuarios, many=True)
#        return Response(serializer.data)
#
#    def post(self, request):
#        serializer = UsuarioSerializer(data=request.data)
#        if serializer.is_valid():
#            usuario = serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        else:
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Listado de detalle de un usuario

#class UsuarioDetalleAPI(APIView):
#
#    def get(self, request, pk):
#        usuario = get_object_or_404(User, pk=pk)
#        serializer = UsuarioSerializer(usuario)
#        return Response(serializer.data)
#
#    def put(self, request, pk):
#        usuario = get_object_or_404(User, pk=pk)
#        serializer = UsuarioSerializer(usuario, data=request.data)
#        if serializer.is_valid():
#            usuario = serializer.save()
#            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#        else:
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    def delete(self, request, pk):
#        usuario = get_object_or_404(User, pk=pk)
#        usuario.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)

#  ----- - - - - - - - - - - - - - --

##API Listado de blogs
from usuarios.serializers import UsuarioSerializer


class UsuariosListaAPI(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UsuarioSerializer



class UsuarioDetalleAPI(RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UsuarioSerializer