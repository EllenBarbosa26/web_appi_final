from rest_framework import viewsets
from .models import Pessoa
from .serializers import PessoaSerializer
from rest_framework.permissions import IsAuthenticated

# ViewSet para listar e criar várias atas
class PessoaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
