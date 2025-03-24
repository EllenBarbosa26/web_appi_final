from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pessoa import views as pessoa_views
from ata import views as ata_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

# Criar um único roteador
router = DefaultRouter()

# Registrar os ViewSets
router.register(r'pessoas', pessoa_views.PessoaViewSet)
router.register(r'atas', ata_views.AtaViewSet)

# Definir as URLs no projeto central
urlpatterns = [
    path('admin/', admin.site.urls),  # Acesso ao admin
    path('api/v1/', include(router.urls)),  # Inclui todas as rotas registradas no roteador

    #\authenticação jwt
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # documentação

    path('api/schema/',SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/',SpectacularSwaggerView.as_view(), name='swagger-ui'),
    path('api/schema/redoc',SpectacularRedocView.as_view(), name='redoc'),

]
