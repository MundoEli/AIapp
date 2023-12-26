from django.contrib import admin
from django.urls import path, include
from text_api.urls import urlpatterns as text_api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('authapp.urls')),
    path('api/v1/text_api/', include(text_api_urls))
]
