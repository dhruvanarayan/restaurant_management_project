from rest_framework import serializers
from .models import MenuCategory

class MenuCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the MenuCategory model.
    """
    class Meta:
        model = MenuCategory
        fields = ['name']