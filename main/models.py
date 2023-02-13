from django.db import models
from django.core.exceptions import ValidationError


def validateGtZero(value):
    if value <= 54:
        raise ValidationError('Price must be greater than 50 cents')


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(validators=[validateGtZero])

    class Meta:
        ordering = ('-price',)

    def __str__(self):
        return f"""Item {self.pk}: "{self.name}" {self.price / 100}$"""
