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
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category_id')
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
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        product.category_id = request.data.get('category_id') # type: ignore
        product.save()
        return Response(status=status.HTTP_200_OK, data=ProductDetailSerializer(product, many=False).data)
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
        name = request.data.get('name')
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
        category.name = request.data.get('name')
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
        text = request.data.get('text')
        product_id = request.data.get('product_id')
        stars = request.data.get('stars')

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
        review.text = request.data.get('text')
        review.product_id = request.data.get('product_id') # type: ignore
        review.stars = request.data.get('stars')
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