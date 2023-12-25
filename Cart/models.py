from django.db import models
import uuid

from User.models import User as User
from Product.models import Product as Product

# Create your models here.

STATUS_CHOICES = {'Submitted': 'Submitted',
                  'Processed': 'Processed'}


class Order(models.Model):
    orderID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    orderDate = models.DateTimeField(auto_now=True, editable=False)
    orderStatus = models.CharField(
        max_length=10, null=True, choices=STATUS_CHOICES)


class Cart(models.Model):
    orderId = models.ForeignKey("Order", on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
