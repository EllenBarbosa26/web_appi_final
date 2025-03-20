from django.db import models

class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    num = models.IntegerField()  # Corrigido para IntegerField
    complemento = models.TextField(blank=True, null=True)  # Permitir campo opcional
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=9)  # Permitir formato 12345-678
    estado = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.rua}, {self.num} - {self.bairro}, {self.cidade}/{self.estado}"

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
        ordering = ["cidade", "bairro", "rua"]  # Ordena primeiro por cidade, depois bairro e rua
        db_table = "enderecos"  # Nome da tabela no banco de dados


class Pessoa(models.Model):
    TIPOS_PESSOAS = [
        ("ALUNO", "Aluno"),
        ("PROFESSOR", "Professor"),
    ]
    
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    pdf = models.FileField(upload_to='pdfs/')
    tipo_pessoa = models.CharField(
        "Tipo de Pessoa", max_length=10, choices=TIPOS_PESSOAS, default="ALUNO"
    )
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, related_name='pessoas', blank=True, null=True
    )

    def __str__(self):
        return f"{self.nome} ({self.tipo_pessoa})"

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        ordering = ["nome"]  # Ordenação alfabética por nome
        db_table = "pessoas"
        constraints = [
            models.UniqueConstraint(fields=["cpf"], name="unique_cpf_pessoa")  # Garante que o CPF seja único
        ]


class ArquivoPDF(models.Model):
    pessoa = models.ForeignKey(
        Pessoa, on_delete=models.CASCADE, related_name='arquivos'
    )
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return f"Arquivo de {self.pessoa.nome}"

    class Meta:
        verbose_name = "Arquivo PDF"
        verbose_name_plural = "Arquivos PDF"
        ordering = ["pessoa__nome"]  # Ordena os arquivos pelo nome da pessoa
        db_table = "arquivos_pdf"
