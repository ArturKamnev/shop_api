from rest_framework import serializers
from .models import Product, Category, Review

class CategoriesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name products_count'.split()

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ReviewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text product stars'.split()


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewForProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars'.split()

class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id title price'.split()


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = 'id title description price category reviews'.split()
        depth = 1

class ProductsWithReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewForProductSerializer(many=True)
    class Meta:
        model = Product
        fields = 'id title description price category reviews rating'.split()