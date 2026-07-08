from django.urls import path
from .views import product_detail_api_view, products_list_create_api_view, review_detail_api_view, reviews_and_products_api_view, reviews_list_create_api_view, categories_list_create_api_view, category_detail_api_view

urlpatterns = [
    path('products/', products_list_create_api_view),
    path('products/<int:id>/', product_detail_api_view),
    path('categories/', categories_list_create_api_view),
    path('categories/<int:id>/', category_detail_api_view),
    path('reviews/', reviews_list_create_api_view),
    path('reviews/<int:id>/', review_detail_api_view),
    path('products/reviews/', reviews_and_products_api_view),
]