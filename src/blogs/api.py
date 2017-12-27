from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView

from blogs.models import Post
from blogs.permissions import PostPermisos, PostDetallesPermisos
from blogs.serializers import PostSerializer, PostDetalleSerializer, PublicarPostSerializer


class ListarPostsAPI(ListAPIView):

    permission_classes = [PostPermisos]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['titulo', 'resumen', 'cuerpo_del_post']
    ordering_fields = ['titulo', 'fecha_de_publicacion']

    def get_queryset(self):
        usuario = self.kwargs['usuario']
        return Post.objects.filter(usuario_id=usuario).order_by('-fecha_publicacion')


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

