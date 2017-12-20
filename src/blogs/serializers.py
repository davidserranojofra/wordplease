from rest_framework import serializers
from blogs.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
      Model = Post
      fields = '__all__'