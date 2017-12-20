
from rest_framework.generics import ListCreateAPIView

from blogs.models import Post
from blogs.serializers import PostSerializer


class ListarPostsAPI(ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
