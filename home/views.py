from rest_framework.generics import ListAPIView
from .models import MenuCategory
from .serializers import MenuCategorySerializer

class MenuCategoryListAPIView(ListAPIView):
    """
    API view to retrieve a list of all menu categories.
    """
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer