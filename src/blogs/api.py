from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, get_object_or_404

from blogs.models import Post
from blogs.permissions import PostPermisos, PostDetallesPermisos
from blogs.serializers import PostSerializer, PostDetalleSerializer, PublicarPostSerializer
from datetime import datetime

class ListarPostsAPI(ListAPIView):

    permission_classes = [PostPermisos]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['titulo', 'resumen', 'cuerpo_del_post']
    ordering_fields = ['titulo', 'fecha_publicacion']

    def get_queryset(self):

        usuario = self.kwargs['usuario']

        if self.request.user.is_authenticated and int(self.request.user.id) == int(usuario) or self.request.user.is_superuser:
            return Post.objects.filter(usuario_id=usuario).order_by('-fecha_publicacion')
        else:
            return Post.objects.filter(usuario_id=usuario, fecha_publicacion__lte=datetime.now()).order_by('-fecha_publicacion')



    def get_serializer_class(self):
        return PostSerializer if self.request.method == 'GET' else PostDetalleSerializer


class PostDetalleAPI(RetrieveUpdateDestroyAPIView):

    queryset =Post.objects.all()
    serializer_class = PostDetalleSerializer
    permission_classes = [PostDetallesPermisos]

    def perform_update(self, serializer):
        serializer.save(usuario=self.request.user)


class PublicarPostAPI(CreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PublicarPostSerializer
    permission_classes = [PostDetallesPermisos]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

