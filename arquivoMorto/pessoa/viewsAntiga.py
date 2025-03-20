from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pessoa
from .serializers import PessoaSerializer
from rest_framework.permissions import IsAuthenticated

class PessoaList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Listar todas as pessoas
        pessoas = Pessoa.objects.all()
        serializer = PessoaSerializer(pessoas, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Criar uma nova pessoa
        serializer = PessoaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PessoaDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        # Obter detalhes de uma pessoa específica
        try:
            pessoa = Pessoa.objects.get(pk=pk)
        except Pessoa.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data)

    def put(self, request, pk):
        # Atualizar uma pessoa específica
        try:
            pessoa = Pessoa.objects.get(pk=pk)
        except Pessoa.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PessoaSerializer(pessoa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Deletar uma pessoa específica
        try:
            pessoa = Pessoa.objects.get(pk=pk)
        except Pessoa.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        pessoa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
