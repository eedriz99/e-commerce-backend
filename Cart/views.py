from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from Cart.models import Order, Cart
from Cart.serializer import CartSerializer, OrderSerializer
from Product.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


# @api_view(['GET', "POST"])
# def cartView(request):
#     if request.method == 'POST':
#         # querySet = Cart.objects.get_or_create()
#         serializer = CartSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'GET':
#         querySet = Cart.objects.all()
#         serializer = CartSerializer(querySet)
#         return Response(serializer.data)


@login_required()
@api_view(['GET'])
def add_to_cart(request, uuid):
    """view to add item to cart"""
    user = request.user
    item = Product.objects.get(pk=uuid)
    order = Order.objects.create(product=item, user_id=user)
    order_item, status = Cart.objects.get_or_create(owner=user, )
    order_item.items.add(order)
    order.save()
    return Response(data={"message": "added to cart successfully"})


@login_required()
@api_view(['GET'])
def remove_from_cart(request, uuid):
    """view to remove an item from the cart"""
    user = request.user.id
    product = get_object_or_404(Product, pk=uuid)
    item = Order.objects.get(product__name=product, user_id=user, )
    cart_item = Cart.objects.get(owner=user)
    cart_item.items.remove(item.id)
    cart_item.save()
    del item
    return Response(data={"message": "Product removed from cart"})


@login_required
@api_view(['GET'])
def view_cart(request):
    cart_item_obj = Cart.objects.get(owner=request.user)
    serialize_data = CartSerializer(cart_item_obj)
    cart_item_list = cart_item_obj.items.all()
    # cart_item_price = sum([item.product.price * item.quantity for item in cart_item_obj.items.all()])

    data = {'cart_items': serialize_data.data, }
    return Response(data=data)
