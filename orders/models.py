# orders/models.py
from django.db import models
from home.models import OrderStatus

class Order(models.Model):
    # ... other fields
    status = models.ForeignKey(
        OrderStatus,
        on_delete=models.SET_NULL,
        null=True
    )
    # ... other methods