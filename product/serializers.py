from rest_framework.serializers import ModelSerializer
from .models import Product, Category, Review

#category

class CategoriesListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'name'.split()

class CategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

#products

class ProductsListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = 'title price'.split()

class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

#reviews

class ReviewsListSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = 'text'[0:50].split()

class ReviewDetailSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'