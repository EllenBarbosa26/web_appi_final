from django.urls import path
from .views import PessoasAPIView, PessoaAPIView

urlpatterns = [
    path('', PessoasAPIView.as_view(), name='pessoas'),  # Lista e cria
    path('<int:pk>/', PessoaAPIView.as_view(), name='pessoa'),  # Detalha, atualiza e deleta
]
