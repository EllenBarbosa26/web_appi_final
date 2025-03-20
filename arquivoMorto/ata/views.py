from rest_framework import generics
from .models import Ata
from .serializers import AtaSerializer

# Lista todas as atas e permite criar novas atas
class AtasAPIView(generics.ListCreateAPIView):  
    queryset = Ata.objects.all()
    serializer_class = AtaSerializer

# Recupera, atualiza ou exclui uma ata específica
class AtaAPIView(generics.RetrieveUpdateDestroyAPIView):  
    queryset = Ata.objects.all()
    serializer_class = AtaSerializer
