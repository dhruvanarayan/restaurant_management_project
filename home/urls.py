from django.urls import path
from .views import *
from .views import MenuCategoryAPIView

urlpatterns = [
    path('api/categories/',MenuCategoryAPIView.as_view(), name = 'api-categories')
]