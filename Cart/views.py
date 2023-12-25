from django.shortcuts import render
from Cart.models import Order, Cart
from Cart.serializer import CartSerializer, OrderSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['GET', "POST"])
def cartView(request):
    if request.method == 'POST':
        # querySet = Cart.objects.get_or_create()
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        querySet = Cart.objects.all()
        serializer = CartSerializer(querySet)
        return Response(serializer.data)
