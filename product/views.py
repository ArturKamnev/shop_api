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
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.

#product

class ProductsApiView(APIView):
    def get(self, request):
        products = Product.objects.all()
        data = ProductsListSerializer(products, many=True).data

        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
    def post(self, request):
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
        
class ProductDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = "id"
    http_method_names = ["get", "put", "delete"]

    def update(self, request, *args, **kwargs):
        product = self.get_object()

        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product.title = serializer.validated_data["title"]
        product.description = serializer.validated_data["description"]
        product.price = serializer.validated_data["price"]
        product.category_id = serializer.validated_data["category_id"]
        product.save()

        return Response(
            ProductDetailSerializer(product).data,
            status=status.HTTP_200_OK,
        )

class CategoriesApiView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        data = CategoriesListSerializer(categories, many=True).data

        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
    def post(self, request):
        serializer = CategoryValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        
        name = serializer.validated_data.get('name') # type: ignore
        category = Category.objects.create(
            name=name
        )
        return Response(status=status.HTTP_201_CREATED, data=CategoryDetailSerializer(category, many=False).data)

class CategoryDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer 
    lookup_field = 'id'

class ReviewsListApiView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        data = ReviewsListSerializer(reviews, many=True).data

        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
    def post(self, request):
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
        
class ReviewDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer
    lookup_field = "id"
    http_method_names = ["get", "put", "delete"]

    def update(self, request, *args, **kwargs):
        review = self.get_object()

        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        review.text = serializer.validated_data["text"]
        review.stars = serializer.validated_data["stars"]
        review.product_id = serializer.validated_data["product_id"]
        review.save()

        return Response(
            ReviewDetailSerializer(review).data,
            status=status.HTTP_200_OK,
        )

class ReviewsAndProductsListApiView(APIView):
    def get(self, request):
        products = Product.objects.all()
        data = ProductsWithReviewsSerializer(products, many=True).data

        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
