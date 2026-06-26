from django.shortcuts import render
from .serializers import ProductsListSerializer, CategoriesListSerializer, ReviewsListSerializer
from .serializers import ProductDetailSerializer, CategoryDetailSerializer, ReviewDetailSerializer
from .serializers import ProductsWithReviewsSerializer
from .models import Product, Category, Review
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

#product

@api_view(http_method_names=['GET'])
def products_list_api_view(request):
    products = Product.objects.all()
    data = ProductsListSerializer(products, many=True).data

    return Response(
        data=data,
        status=status.HTTP_200_OK
    )

@api_view(http_method_names=['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    data = ProductDetailSerializer(product, many=False).data
    return Response(
        data=data,
        status=status.HTTP_200_OK
    )

#category

@api_view(http_method_names=['GET'])
def categories_list_api_view(request):
    categories = Category.objects.all()
    data = CategoriesListSerializer(categories, many=True).data

    return Response(
        data=data,
        status=status.HTTP_200_OK
    )

@api_view(http_method_names=['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
    
    data = CategoryDetailSerializer(category, many=False).data
    return Response(
        data=data,
        status=status.HTTP_200_OK
    )

#review

@api_view(http_method_names=['GET'])
def reviews_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewsListSerializer(reviews, many=True).data

    return Response(
        data=data,
        status=status.HTTP_200_OK
    )

@api_view(http_method_names=['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'review not found'}, status=status.HTTP_404_NOT_FOUND)
    
    data = ReviewDetailSerializer(review, many=False).data
    return Response(
        data=data,
        status=status.HTTP_200_OK
    )

@api_view(http_method_names=['GET'])
def reviews_and_products_api_view(request):
    products = Product.objects.all()
    data = ProductsWithReviewsSerializer(products, many=True).data

    return Response(
        data=data,
        status=status.HTTP_200_OK
    )