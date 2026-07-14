from django.urls import path
from .views import ProductDetailApiView, ProductsApiView, CategoriesApiView, CategoryDetailApiView, ReviewDetailApiView, ReviewsListApiView, ReviewsAndProductsListApiView
urlpatterns = [
    path('products/', ProductsApiView.as_view()),
    path('products/<int:id>/', ProductDetailApiView.as_view()),
    path('categories/', CategoriesApiView.as_view()),
    path('categories/<int:id>/', CategoryDetailApiView.as_view()),
    path('reviews/', ReviewsListApiView.as_view()),
    path('reviews/<int:id>/', ReviewDetailApiView.as_view()),
    path('products/reviews/', ReviewsAndProductsListApiView.as_view()),
]