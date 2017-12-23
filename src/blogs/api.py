from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from blogs.models import Post
from blogs.serializers import PostSerializer, PostDetalleSerializer


class ListarPostsAPI(ListCreateAPIView):

    queryset = Post.objects.all()

    def get_serializer_class(self):
        return PostSerializer if self.request.method == 'GET' else PostDetalleSerializer


class PostDetalleAPI(RetrieveUpdateDestroyAPIView):

    queryset =Post.objects.all()
    serializer_class = PostDetalleSerializer

