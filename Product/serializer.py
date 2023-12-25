# from django.contrib.auth.models import Group, User
from Product.models import Product
from rest_framework import serializers



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ['productId']
        # read_only_fields = ['productNo']
