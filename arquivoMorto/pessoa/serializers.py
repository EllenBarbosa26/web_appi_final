from rest_framework import serializers
from .models import Endereco, Pessoa

# Serializer para o modelo Endereco
class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__' 

# Serializer para o modelo Pessoa
class PessoaSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()  
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'cpf', 'pdf', 'tipo_pessoa', 'endereco']  

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco')
        endereco = Endereco.objects.create(**endereco_data)
        pessoa = Pessoa.objects.create(endereco=endereco, **validated_data)
        return pessoa


    def update(self, instance, validated_data):
        # Atualiza a pessoa e o endereço 
        
        endereco_data = validated_data.pop('endereco', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if endereco_data:
            # Atualiza o endereço associado
            endereco = instance.endereco
            for attr, value in endereco_data.items():
                setattr(endereco, attr, value)
            endereco.save()
        instance.save()
        return instance
