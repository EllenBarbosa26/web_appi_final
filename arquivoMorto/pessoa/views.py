from rest_framework import generics
from .models import Pessoa
from .serializers import PessoaSerializer

class PessoasAPIView(generics.ListCreateAPIView):  # CORRETO para listar e criar
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class PessoaAPIView(generics.RetrieveUpdateDestroyAPIView):  # CORRETO para um objeto específico
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
