from django.contrib import admin
from .models import Ata, ArquivoPDF

@admin.register(Ata)
class AtaAdmin(admin.ModelAdmin):
    list_display = ("ano", "serie", "turma")  # Exibe esses campos na listagem
    list_filter = ("ano", "serie", "turma")  # Permite filtrar por ano, série e turma
    ordering = ("ano", "serie", "turma")  # Ordenação padrão

@admin.register(ArquivoPDF)
class ArquivoPDFAdmin(admin.ModelAdmin):
    list_display = ("ata", "nome")  # Exibe o nome do arquivo e a ata associada
    ordering = ("ata",)  # Ordena os arquivos por ata
