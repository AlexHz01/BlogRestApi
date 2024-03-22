from rest_framework.viewsets import ModelViewSet

from posts.api.serializers import PostSerializer
from posts.models import Post
from django_filters.rest_framework import DjangoFilterBackend

class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'category__title']
