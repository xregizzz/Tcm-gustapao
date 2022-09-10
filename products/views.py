from rest_framework import generics

from .models import Ingredient, Product, Category
from .permissions import IsStaffOrAdminOrReadOnly
from .serializers import IngredientsSerializer, ProductSerializer, CategorySerializer

# Criacao de produto por admin e listagem geral de produtos publica
class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsStaffOrAdminOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Listagem de produto por id publico, update e delete por admin
class ProductDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsStaffOrAdminOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class IngredientsListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsStaffOrAdminOrReadOnly]
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializer


class IngredientDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializer

class CategoryView(generics.ListCreateAPIView):
    permission_classes = [IsStaffOrAdminOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer