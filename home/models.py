from django.db import models

class MenuCategory(models.Model):
    """
    Represents categories for restaurant menu items like
    'Appetizers', 'Main Courses', 'Desserts'.
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Menu Categories"

    def __str__(self):
        return self.name