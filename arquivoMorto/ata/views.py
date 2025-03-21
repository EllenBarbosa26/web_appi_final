from rest_framework import viewsets
from .models import Ata
from .serializers import AtaSerializer

class AtaViewSet(viewsets.ModelViewSet):
    queryset = Ata.objects.all()  # Retorna todas as instâncias de Ata
    serializer_class = AtaSerializer  # Usando o serializador de Ata
