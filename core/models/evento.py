from django.db import models
from uploader.models import Image


from core.models.instituicao import Instituicao

class Evento(models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateField(max_length=255)
    hora = models.TimeField(max_length=255)
    local = models.CharField(max_length=255)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.PROTECT, related_name="instituicao")
    observacoes = models.CharField(max_length=500, blank=True, null=True) 
    data_inscricao_inicio = models.DateField()
    data_inscricao_fim = models.DateField()
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.nome