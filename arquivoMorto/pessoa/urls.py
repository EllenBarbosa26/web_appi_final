from rest_framework import viewsets
from .models import Pessoa
from .serializers import PessoaSerializer
# ViewSet para listar e criar várias atas

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
