from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import FoodType, Food, Comment
from .serializers import FoodTypeSerializer, FoodSerializer, CommentSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.throttling import UserRateThrottle
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from django.core.mail import send_mail



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



class FoodTypeViewSet(viewsets.ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    permission_classes = [IsAuthenticated] 
    throttle_classes = [UserRateThrottle]  

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated] 
    throttle_classes = [UserRateThrottle]  
class CommentViewSet(viewsets.ModelViewSet)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]  



def send_comment_email(self, request, pk=None):
        comment = self.get_object()
        subject = f'New Comment on {comment.food.nomi}'
        message = f'Comment: {comment.text}\nBy: {comment.author}'
        recipient_list = [settings.EMAIL_HOST_USER] 
        
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
            return Response({"message": "Email sent successfully."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    