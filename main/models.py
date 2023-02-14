from django.db import models
from django.core.exceptions import ValidationError
import stripe


def validateGtCents(value):
    if value <= 50:
        raise ValidationError('Price must be greater than 50 cents')


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField(validators=[validateGtCents])

    class Meta:
        ordering = ('price',)

    def __str__(self):
        return f"""Item {self.pk}: "{self.name}" {self.price / 100}$"""


class OrderItem(models.Model):
    order = models.ForeignKey(
        'Order', on_delete=models.CASCADE, related_name='orderItems')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Order {self.order.pk}: {self.item.name} - {self.quantity}"


class Order(models.Model):
    STATUS_CHOICES = (
        ("new", "New order"),
        ("in_progress", "In progress"),
        ("complited", "Complited")
    )

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="new")

    def __str__(self):
        return f"{self.pk}: {self.status}"
