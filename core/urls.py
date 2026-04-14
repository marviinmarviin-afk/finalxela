from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views # Importación para los tokens

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-token-auth/', views.obtain_auth_token), # Esta es la "llave" para Flutter
]