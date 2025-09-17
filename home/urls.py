from django.urls import path
from .views import MenuCategoryListAPIView

urlpatterns = [
    # Example URL: /api/menu-categories/
    path('api/menu-categories/', MenuCategoryListAPIView.as_view(), name='menu-category-list'),
]