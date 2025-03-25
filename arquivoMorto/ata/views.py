from rest_framework import viewsets
from .models import Ata
from .serializers import AtaSerializer
from rest_framework.permissions import IsAuthenticated

class AtaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Ata.objects.all()  # Retorna todas as instâncias de Ata
    serializer_class = AtaSerializer 
