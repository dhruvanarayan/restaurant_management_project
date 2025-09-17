# home/views.py

from rest_framework.generics import ListAPIView
from .models import OrderStatus
from .serializers import OrderStatusSerializer

class OrderStatusAPIView(ListAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer