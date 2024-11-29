from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import FoodType, Food, Comment
from .serializers import FoodTypeSerializer, FoodSerializer, CommentSerializer
from rest_framework.filters import SearchFilter, OrderingFilter

class FoodTypeListCreateView(generics.ListCreateAPIView):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    permission_classes = [IsAuthenticated] 
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['nomi'] 
    ordering_fields = ['nomi']  
    ordering = ['nomi']  


class FoodListCreateView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]  
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['nomi', 'tarkibi']  
    ordering_fields = ['narxi']  
    ordering = ['narxi'] 





class FoodTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    permission_classes = [IsAuthenticated] 


class FoodRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]  





class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]  
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['text', 'author']
    ordering_fields = ['created']  
    ordering = ['created']  


class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
