from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('authapp.urls')),
    path('api/v1/meal_app/', include('meal_app.urls'))
]
