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

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ("rua", "bairro", "cidade", "estado", "cep")  # Exibe os campos na listagem
    search_fields = ("rua", "bairro", "cidade", "estado", "cep")  # Permite busca por rua, bairro, cidade, estado e cep
    ordering = ("cidade", "bairro", "rua")  # Ordena primeiro por cidade, depois bairro e rua

@admin.register(ArquivoPDF)
class ArquivoPDFAdmin(admin.ModelAdmin):
    list_display = ("pessoa", "pdf")  # Exibe pessoa e arquivo PDF
    search_fields = ("pessoa__nome",)  # Permite buscar pelo nome da pessoa associada ao arquivo
    ordering = ("pessoa__nome",)  # Ordena os arquivos pelo nome da pessoa associada
