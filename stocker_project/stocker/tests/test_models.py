from ..models import Unidade, Insumo
from django.test import TestCase


class ModelUnidadeTest(TestCase):
    def test_unidade_nome(self):
        kilo = Unidade(nome='Kilogramas')
        kilo.save()
        self.assertEqual((kilo.nome == 'Kilogramas'), True)


class ModelInsumoTest(TestCase):
    def test_insumo_quantidade_positiva(self):
        kilo = Unidade(nome='Kilogramas')
        kilo.save()
        ins = Insumo(nome='Arroz',quantidade='30',ativo=True,unidade=kilo)
        ins.save()
        self.assertEqual((ins.nome == 'Arroz'), True)
        self.assertEqual((ins.quantidade == '30'), True)
        self.assertEqual((ins.ativo == True), True)
        self.assertEqual((ins.unidade.nome == kilo.nome), True)
    def test_insumo_quantidade_negativa(self):
        kilo = Unidade(nome='Kilogramas')
        kilo.save()
        ins = Insumo(nome='Arroz', quantidade='-5', ativo=True, unidade=kilo)
        ins.save()
        self.assertEqual((ins.quantidade == '-5'), True)
