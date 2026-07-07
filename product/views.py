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
# Create your views here.

#product

@api_view(http_method_names=['GET', "POST"])
def products_list_create_api_view(request):
    if request.method == "GET":
        products = Product.objects.all()
        data = ProductsListSerializer(products, many=True).data

        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
    elif request.method == "POST":
        serializer = ProductValidateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        title = serializer.validated_data.get('title') # type: ignore
        description = serializer.validated_data.get('description') # type: ignore
        price = serializer.validated_data.get('price') # type: ignore
        category_id = serializer.validated_data.get('category_id') # type: ignore
        
        with transaction.atomic():
            product = Product.objects.create(
                title=title,
                description=description,
                price=price,
                category_id=category_id
            )
            return Response(status=status.HTTP_201_CREATED, data=ProductDetailSerializer(product, many=False).data)
        

@api_view(http_method_names=['GET', "PUT", "DELETE"])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        data = ProductDetailSerializer(product, many=False).data
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
    elif request.method == "PUT":
        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product.title = serializer.validated_data.get('title') # type: ignore
        product.description = serializer.validated_data.get('description') # type: ignore
        product.price = serializer.validated_data.get('price') # type: ignore
        product.category_id = serializer.validated_data.get('category_id') # type: ignore
        product.save()
        return Response(status=status.HTTP_201_CREATED, data=ProductDetailSerializer(product, many=False).data)
    elif request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#category

@api_view(http_method_names=['GET', "POST"])
def categories_list_create_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        data = CategoriesListSerializer(categories, many=True).data

        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
    elif request.method == "POST":
        serializer = CategoryValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        
        name = serializer.validated_data.get('name') # type: ignore
        category = Category.objects.create(
            name=name
        )
        return Response(status=status.HTTP_201_CREATED, data=CategoryDetailSerializer(category, many=False).data)

@api_view(http_method_names=['GET', "PUT", "DELETE"])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        data = CategoryDetailSerializer(category, many=False).data
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
    elif request.method == "PUT":
        serializer = CategoryValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        category.name = serializer.validated_data.get('name') # type: ignore
        category.save()
        return Response(status=status.HTTP_201_CREATED, data=CategoryDetailSerializer(category, many=False).data)
    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#review

@api_view(http_method_names=['GET', "POST"])
def reviews_list_create_api_view(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        data = ReviewsListSerializer(reviews, many=True).data

        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
    elif request.method == "POST":
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        text = serializer.validated_data.get('text') # type: ignore
        product_id = serializer.validated_data.get('product_id') # type: ignore
        stars = serializer.validated_data.get('stars') # type: ignore

        review = Review.objects.create(
            text=text,
            product_id=product_id,
            stars=stars
        )
        return Response(status=status.HTTP_201_CREATED, data=ReviewDetailSerializer(review, many=False).data)

@api_view(http_method_names=['GET', "PUT", "DELETE"])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'review not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        data = ReviewDetailSerializer(review, many=False).data
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
    elif request.method == "PUT":
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        review.text = serializer.validated_data.get('text') # type: ignore
        review.product_id = serializer.validated_data.get('product_id') # type: ignore
        review.stars = serializer.validated_data.get('stars') # type: ignore
        review.save()
        return Response(status=status.HTTP_201_CREATED, data=ReviewDetailSerializer(review, many=False).data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(http_method_names=['GET'])
def reviews_and_products_api_view(request):
    products = Product.objects.all()
    data = ProductsWithReviewsSerializer(products, many=True).data

    return Response(
        data=data,
        status=status.HTTP_200_OK
    )