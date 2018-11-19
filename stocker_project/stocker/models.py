from django.db import models

class Insumo(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    quantidade = models.IntegerField(default=0)
    ativo = models.BooleanField(default=1)
    data = models.DateField(auto_now=True)
    def __str__(self):
        return self.nome

class Unidade(models.Model):
    insumo = models.ForeignKey(Insumo)
    nome = models.CharField(max_length=128)
    def __str__(self):
        return self.nome