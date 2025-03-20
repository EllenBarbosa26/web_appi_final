from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ata
from .serializers import AtaSerializer
from rest_framework.permissions import IsAuthenticated

class AtaList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Listar todas as atas
        atas = Ata.objects.all()
        serializer = AtaSerializer(atas, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Criar uma nova ata
        serializer = AtaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AtaDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        # Obter detalhes de uma ata específica
        try:
            ata = Ata.objects.get(pk=pk)
        except Ata.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AtaSerializer(ata)
        return Response(serializer.data)

    def put(self, request, pk):
        # Atualizar uma ata específica
        try:
            ata = Ata.objects.get(pk=pk)
        except Ata.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AtaSerializer(ata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Deletar uma ata específica
        try:
            ata = Ata.objects.get(pk=pk)
        except Ata.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        ata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
