from django.urls import path
from .views import FetchTextView, EditTextAPIView

urlpatterns = [
    path('fetch-text/', FetchTextView.as_view(), name='fetch-text'),
    path('edit-text/<int:pk>/', EditTextAPIView.as_view(), name='edit-text'),
]
