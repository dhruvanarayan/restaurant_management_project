from rest_framework import serializers
from .models import MenuCategory

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id', 'name']