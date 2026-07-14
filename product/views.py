from django.shortcuts import render
from .serializers import ProductsListSerializer, CategoriesListSerializer, ReviewsListSerializer
from .serializers import ProductDetailSerializer, CategoryDetailSerializer, ReviewDetailSerializer
from .serializers import ProductsWithReviewsSerializer
from .serializers import ProductValidateSerializer, ReviewValidateSerializer, CategoryValidateSerializer
from .models import Product, Category, Review
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
# Create your views here.

#product

class ProductsApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductsListSerializer
        else:
            return ProductValidateSerializer
        
class ProductDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'

class CategoriesApiView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesListSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CategoriesListSerializer
        else:
            return CategoryValidateSerializer

class CategoryDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer 
    lookup_field = 'id'

class ReviewsListApiView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsListSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReviewsListSerializer
        else:
            return ReviewValidateSerializer
        
class ReviewDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer
    lookup_field = 'id'

class ReviewsAndProductsListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsWithReviewsSerializer
