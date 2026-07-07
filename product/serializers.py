from rest_framework import serializers
from .models import Product, Category, Review
from rest_framework.exceptions import ValidationError

class CategoriesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name products_count'.split()

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100, min_length=1)

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

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, max_length=300, min_length=1)
    stars = serializers.IntegerField(required=True)
    product_id = serializers.IntegerField(required=True)

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError("product does not exists")
        return product_id

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

class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=100, min_length=1)
    description = serializers.CharField(required=True, max_length=300, min_length=1)
    price = serializers.FloatField(required=True)
    category_id = serializers.IntegerField(required=True)
    reviews = serializers.ListField(child=ReviewValidateSerializer())

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category not found')
        return category_id
