from django.test import TestCase
from .models import Unidade, Insumo
from django.core.urlresolvers import reverse

class ModelsTest(TestCase):
    def test_unidade_nome(self):
        kilo = Unidade(nome='Kilogramas')
        kilo.save()
        self.assertEqual((kilo.nome == 'Kilogramas'), True)
    def test_unidade_nome_com_numero(self):
        num = Unidade(nome='123')
        num.save()
        self.assertEqual((num.nome == '123'), True)
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





# def add_cat(nome, quantidade):
#     c = Insumo.objects.get_or_create(nome=nome)[0]
#     c.quantidade = quantidade
#     c.save()
#     return c
#
#
# class IndexViewTest(TestCase):
#
#     def test_index_view_sem_insumos(self):
#         response = self.client.get(reverse('listar_insumos'))
#         self.assertEqual(response.status_code, 200)
#
#     def test_index_view_with_categories(self):
#         add_cat('test', 30)
#         add_cat('temp', 1)
#         add_cat('tmp', 4)
#         add_cat('tmp test temp', 20)
#         response = self.client.get(reverse('listar_insumos'))
#         self.assertEqual(response.status_code, 200)
