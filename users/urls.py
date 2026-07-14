from django.urls import path
from .views import RegistrationApiView, AuthenticationApiView, ConfirmApiView

urlpatterns = [
    path('registration/', RegistrationApiView.as_view()),
    path('authentication/', AuthenticationApiView.as_view()),
    path('confirm/', ConfirmApiView.as_view())
]