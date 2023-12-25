from django.shortcuts import render
from django.http import HttpResponse
from Product.models import Product
from Product.serializer import ProductSerializer

from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
# Create your views here.


def productList(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def productDetail(request, slug='1'):
    try:
        product = Product.objects.get(productNo=int(slug))
        return render(request, "product.html", {'product': product})
    except:
        return HttpResponse(f"Error {Exception}")


@api_view(['GET'])
def all_products(request):
    querySet = Product.objects.all().order_by('productNo')
    serializer = ProductSerializer(querySet, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_paginated_products(request):
    paginator = PageNumberPagination()
    querySet = Product.objects.all().order_by('productNo')
    result = paginator.paginate_queryset(querySet, request)

    if result is not None:
        serializer = ProductSerializer(result, many=True)
        # return Response(serializer.data)
        return paginator.get_paginated_response(serializer.data)


@api_view(['GET', 'POST'])
def single_product(request, slug):
    if request.method == 'GET':
        queryset = Product.objects.get_or_create(productNo=int(slug))[0]
        serializer = ProductSerializer(queryset, many=False)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(request.method, status=status.HTTP_400_BAD_REQUEST)
