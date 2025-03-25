

from rest_framework import serializers
from .models import Ata

# Serializer para o modelo Ata
class AtaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ata
        fields = ['id', 'ano', 'serie', 'turma', 'pdf']  # Campos que serão serializados