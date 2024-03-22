from rest_framework.viewsets import ModelViewSet
from comments.api.serialziers import ComentSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from comments.models import Comment
from comments.api.permissions import IsOwnerOrReadOnly


class CommentModelViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = ComentSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ('-created_at',)
    filterset_fields = ['post']