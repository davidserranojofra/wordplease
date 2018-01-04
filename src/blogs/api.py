from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Q
from blogs.models import Post
from blogs.permissions import PostPermisos
from blogs.serializers import PostDetalleSerializer, PublicarPostSerializer
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



class PostDetalleAPI(RetrieveUpdateDestroyAPIView):

    queryset =Post.objects.all()
    serializer_class = PostDetalleSerializer
    permission_classes = [PostPermisos]


    def get_queryset(self):

        numero_usuario = self.request.user.id

        if self.request.user.is_superuser:
            return Post.objects.order_by('-fecha_publicacion')
        elif self.request.user.is_authenticated:
            return Post.objects.filter(Q(fecha_publicacion__lte=datetime.now()) | Q(usuario_id=numero_usuario))
        else:
            return Post.objects.filter(fecha_publicacion__lte=datetime.now())

    def perform_update(self, serializer):
        serializer.save(usuario=self.request.user)



class PublicarPostAPI(CreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PublicarPostSerializer
    permission_classes = [PostPermisos]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)