from django.urls import path
from .views import UserRegistrationView, CustomUserLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', CustomUserLoginView.as_view())
]
