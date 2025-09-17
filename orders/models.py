from django.db import models
# from django.contrib.auth.models import User # Optional: to link orders to users

class OrderStatus(models.Model):
    """
    Represents the status of an order, e.g., 'Pending', 'Processing', 'Completed'.
    """
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Order Statuses"

    def __str__(self):
        return self.name

class Order(models.Model):
    """
    Represents a customer's order.
    """
    # Example fields:
    # customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # This is the foreign key field required by your task
    status = models.ForeignKey(
        OrderStatus,
        on_delete=models.SET_NULL, # If a status is deleted, set this field to NULL
        null=True,                # Allows the status field to be empty in the database
        blank=True                # Allows the field to be empty in forms
    )

    def __str__(self):
        return f"Order #{self.id} - {self.status.name if self.status else 'No Status'}"

class Coupon(models.Model):
    """
    Represents a discount coupon.
    """
    code = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    # You could add other fields like discount_amount, valid_until, etc.

    def __str__(self):
        return self.code