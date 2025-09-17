from django.urls import path
from .views import *
from .views import OrderStatusAPIView

urlpatterns = [
    path('api/categories/', OrderStatusAPIView.as_view(), name='api-categories'),
]