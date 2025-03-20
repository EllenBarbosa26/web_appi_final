from rest_framework import serializers
from .models import Endereco, Pessoa

# Serializer para o modelo Endereco
class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'  # Inclui todos os campos do modelo

# Serializer para o modelo Pessoa
class PessoaSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()  # Permite editar o endereço junto com a pessoa

    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'cpf', 'pdf', 'tipo_pessoa', 'endereco']  # Campos da pessoa e o endereço

    def create(self, validated_data):
        # Criar uma pessoa e o endereço relacionado
        endereco_data = validated_data.pop('endereco')  # Extrai os dados do endereço
        pessoa = Pessoa.objects.create(**validated_data)  # Cria a pessoa
        endereco = Endereco.objects.create(pessoa=pessoa, **endereco_data)  # Cria o endereço e associa à pessoa
        return pessoa

    def update(self, instance, validated_data):
        # Atualiza a pessoa e o endereço, se necessário
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
