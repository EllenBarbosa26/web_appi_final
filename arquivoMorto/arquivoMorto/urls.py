from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pessoa import views as pessoa_views
from ata import views as ata_views

# Criar um único roteador
router = DefaultRouter()

# Registrar os ViewSets
router.register(r'pessoas', pessoa_views.PessoaViewSet)
router.register(r'atas', ata_views.AtaViewSet)

# Definir as URLs no projeto central
urlpatterns = [
    path('admin/', admin.site.urls),  # Acesso ao admin
    path('api/v1/', include(router.urls)),  # Inclui todas as rotas registradas no roteador
    path('auth/', include('rest_framework.urls')),  # URLs de autenticação do DRF
]
