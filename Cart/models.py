from django.contrib.auth.models import User
from django.db import models
import uuid

from Product.models import Product as Product

# Create your models here.

STATUS_CHOICES = {'Submitted': 'Submitted',
                  'Processed': 'Processed'}


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.product}'


class Cart(models.Model):
    orderID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(Order)
    date_add = models.DateField(auto_now=True, )

    def get_cart_item(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([items.product.price for items in self.items.all()])

    def __str__(self):
        return f'{self.owner} {self.orderID}'
