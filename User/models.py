from django.db import models
import uuid

# Create your models here.


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    profile_picture = models.ImageField()