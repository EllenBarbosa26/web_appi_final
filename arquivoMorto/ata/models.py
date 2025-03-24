from django.db import models

class Ata(models.Model):
    SERIES = [
        ('1', '1º ano'), ('2', '2º ano'), ('3', '3º ano'),
        ('4', '4º ano'), ('5', '5º ano'), ('6', '6º ano')
    ]
    TURMAS = [
        ('A', 'Turma A'), ('B', 'Turma B'), ('C', 'Turma C'),
        ('D', 'Turma D'), ('E', 'Turma E'), ('F', 'Turma F')
    ]

    ano = models.IntegerField("Ano")
    serie = models.CharField("Série", max_length=50, choices=SERIES)
    turma = models.CharField("Turma", max_length=50, choices=TURMAS)
    pdf = models.FileField("Arquivo PDF", upload_to='atas/', null=True, blank=True)

    class Meta:
        verbose_name = "Ata"
        verbose_name_plural = "Atas"
        unique_together = ('ano', 'serie', 'turma')  # Garante que uma ata única seja cadastrada por série/turma no mesmo ano

    def __str__(self):
        return f"Ata {self.ano} - {self.serie} - {self.turma}"


class ArquivoPDF(models.Model):
    ata = models.ForeignKey(Ata, on_delete=models.CASCADE, related_name='arquivos', verbose_name="Ata Relacionada")
    pdf = models.FileField("Arquivo PDF", upload_to='pdfs/')
    nome = models.CharField("Nome do Arquivo", max_length=255, blank=True)

    class Meta:
        verbose_name = "Arquivo PDF"
        verbose_name_plural = "Arquivos PDF"

    def __str__(self):
        return self.nome if self.nome else f'PDF {self.id}'

