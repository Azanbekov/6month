from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsModerator
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsModerator]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

