from django.urls import path
from meal_app import views

urlpatterns = [
    path('', views.get_meals, name="get_meals"),
]
