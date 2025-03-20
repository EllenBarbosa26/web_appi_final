from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Acesso ao admin
    path('api/v1/pessoas/', include('pessoa.urls')),  # URLs para o app pessoa
    path('api/v1/atas/', include('ata.urls')),  # URLs para o app ata
    path('auth/', include('rest_framework.urls')),  # URLs de autenticação do DRF
]
