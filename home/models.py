from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    name =models.CharField(max_length = 100, unique = True)
    
    class Meta:
        verbose_name_plural = "Menu Categories"

    def __str__(self):
        return self.name 