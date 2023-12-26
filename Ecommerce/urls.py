"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Product import views as product_views
from Cart import views as cart_views
# from rest_framework import routers

# router = routers.SimpleRouter()

# router.register(r'products', views.MyViewSet, basename="products")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', product_views.productList, name='product-list'),
    path('product/<slug:slug>', product_views.productDetail, name='product-detail'),
    path('productsview/', product_views.all_products, name='all-products'),
    path('productdetail/<slug:slug>',
         product_views.single_product, name='single-product'),
    path('paginatedproducts/', product_views.get_paginated_products,
         name='paginated-products'),
    path('cart/view', cart_views.view_cart, name='cart-view'),
    path('cart/add/<str:uuid>', cart_views.add_to_cart, name="add_to_cart"),
    path('cart/remove/<str:uuid>', cart_views.remove_from_cart,
         name='remove_from_cart'),
    # path('', include(router.urls))
]


# urlpatterns += router.urls
