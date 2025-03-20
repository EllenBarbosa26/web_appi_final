from django.urls import path
from .views import AtasAPIView, AtaAPIView

urlpatterns = [
    path('', AtasAPIView.as_view(), name='atas'),  # Lista todas as atas e permite criar novas
    path('<int:pk>/', AtaAPIView.as_view(), name='ata'),  # Recupera, atualiza ou exclui uma ata específica
]
