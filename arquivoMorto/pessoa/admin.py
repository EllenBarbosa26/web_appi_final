from django.contrib import admin
from .models import Pessoa, Endereco, ArquivoPDF

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf", "tipo_pessoa", "endereco")  # Exibe os campos na listagem
    list_filter = ("tipo_pessoa", "endereco")  # Filtro por tipo de pessoa e endereço
    search_fields = ("nome", "cpf")  # Permite buscar pelo nome e CPF
    ordering = ("nome",)  # Ordenação padrão por nome
    readonly_fields = ("cpf",)  # Torna o CPF um campo somente leitura
    fieldsets = (
        (None, {
            'fields': ('nome', 'cpf', 'tipo_pessoa', 'endereco', 'pdf')
        }),
    )


