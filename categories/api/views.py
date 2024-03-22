from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from .serializer import CategorySerialzier
from .permission import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class CategoryModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()
    # queryset = Category.objects.filter(published=True)
    serializer_class = CategorySerialzier
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published']