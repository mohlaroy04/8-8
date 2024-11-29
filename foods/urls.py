from django.urls import path, include
from .views import FoodTypeListCreateView, FoodTypeRetrieveUpdateDestroyView, FoodListCreateView, FoodRetrieveUpdateDestroyView, CommentListCreateView, CommentRetrieveUpdateDestroyView, FoodTypeViewSet, FoodViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'food-types', FoodTypeViewSet)
router.register(r'foods', FoodViewSet)
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('food-types/', FoodTypeListCreateView.as_view(), name='food_type_list_create'),
    path('food-types/<int:pk>/', FoodTypeRetrieveUpdateDestroyView.as_view(), name='food_type_retrieve_update_destroy'),
    path('foods/', FoodListCreateView.as_view(), name='food_list_create'),
    path('foods/<int:pk>/', FoodRetrieveUpdateDestroyView.as_view(), name='food_retrieve_update_destroy'),
    path('comments/', CommentListCreateView.as_view(), name='comment_list_create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment_retrieve_update_destroy'),
]