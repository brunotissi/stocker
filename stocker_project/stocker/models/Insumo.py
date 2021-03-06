from django.db import models
from .Unidade import Unidade


class Insumo(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    quantidade = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)
    data = models.DateField(auto_now=True)
    unidade = models.ForeignKey(Unidade, blank=True, null=True)
    def __str__(self):
        return self.nome