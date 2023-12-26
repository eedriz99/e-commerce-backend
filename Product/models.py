from django.db import models
import uuid
# Create your models here.


class Product(models.Model):
    productId = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    productNo = models.IntegerField(unique=True, primary_key=False)
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=50, default="Unknown")
    image = models.URLField()

    def __str__(self):
        return f'{self.name}'

