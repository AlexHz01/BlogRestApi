from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from .serializer import CategorySerialzier
from .permission import IsAdminOrReadOnly

class CategoryModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerialzier