from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from blogs.models import Post
from blogs.permissions import PostPermisos
from blogs.serializers import PostSerializer, PostDetalleSerializer



class ListarPostsAPI(ListCreateAPIView):

    queryset = Post.objects.all().order_by('-fecha_publicacion')
    permission_classes = [PostPermisos]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['titulo', 'resumen', 'cuerpo_del_post']
    ordering_fields = ['titulo', 'fecha_de_publicacion']

    def get_serializer_class(self):
        return PostSerializer if self.request.method == 'GET' else PostDetalleSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class PostDetalleAPI(RetrieveUpdateDestroyAPIView):

    queryset =Post.objects.all()
    serializer_class = PostDetalleSerializer
    permission_classes = [PostPermisos]

    def perform_update(self, serializer):
        serializer.save(usuario=self.request.user)

