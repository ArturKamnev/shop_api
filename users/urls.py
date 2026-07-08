from django.urls import path
from .views import registration_api_view, authentication_api_view, confirm_api_view

urlpatterns = [
    path('registration/', registration_api_view),
    path('authentication/', authentication_api_view),
    path('confirm/', confirm_api_view)
]