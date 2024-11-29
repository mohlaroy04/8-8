from django.urls import path
from .views import FoodTypeListCreateView, FoodTypeDetailView, FoodListCreateView, FoodDetailView, CommentListCreateView, CommentDetailView

urlpatterns = [
    path('foodtypes/', FoodTypeListCreateView.as_view()),
    path('foodtypes/<int:pk>/', FoodTypeDetailView.as_view()),
    path('foods/', FoodListCreateView.as_view()),
    path('foods/<int:pk>/', FoodDetailView.as_view()),
    path('comments/', CommentListCreateView.as_view()),
    path('comments/<int:pk>/', CommentDetailView.as_view()),
]