from .test_models import ModelUnidadeTest, ModelInsumoTest
#from .test_view import ViewsTest
from .test_forms import UnidadeFormTest, InsumoFormTest
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
