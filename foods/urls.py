from django.urls import path
from .views import FoodTypeListCreateView, FoodTypeRetrieveUpdateDestroyView, FoodListCreateView, FoodRetrieveUpdateDestroyView, CommentListCreateView, CommentRetrieveUpdateDestroyView

urlpatterns = [
    path('food-types/', FoodTypeListCreateView.as_view(), name='food_type_list_create'),
    path('food-types/<int:pk>/', FoodTypeRetrieveUpdateDestroyView.as_view(), name='food_type_retrieve_update_destroy'),
    path('foods/', FoodListCreateView.as_view(), name='food_list_create'),
    path('foods/<int:pk>/', FoodRetrieveUpdateDestroyView.as_view(), name='food_retrieve_update_destroy'),
    path('comments/', CommentListCreateView.as_view(), name='comment_list_create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment_retrieve_update_destroy'),
]
