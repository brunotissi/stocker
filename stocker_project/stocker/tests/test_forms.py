from django.test import TestCase
from ..models import Unidade, Insumo
from django.contrib.auth.models import User
from ..forms import InsumoForm,UnidadeForm,UserForm,EditInsumoForm


class UnidadeFormTest(TestCase):
    def test_valid_form(self):
        w = Unidade.objects.create(nome='Kilo')
        data = {'nome': w.nome}
        form = UnidadeForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w = Unidade.objects.create(nome='')
        data = {'nome': w.nome}
        form = UnidadeForm(data=data)
        self.assertFalse(form.is_valid())

class InsumoFormTest(TestCase):


    def test_invalid_form(self):
        kilo = Unidade.objects.create(nome='Kilo')
        w = Insumo.objects.create(nome='Arroz',quantidade='20',unidade=kilo)
        data = {'nome': w.nome,'quantidade' : w.quantidade,'unidade' : w.unidade}
        form = InsumoForm(data=data)
        self.assertFalse(form.is_valid())

class EditInsumoFormTest(TestCase):
    def test_valid_form(self):
        data = {'quantidade' : 100}
        form = EditInsumoForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'quantidade' : 'String'}
        form = UnidadeForm(data=data)
        self.assertFalse(form.is_valid())

class UserFormTest(TestCase):

    def test_invalid_form(self):
        w = User.objects.create(username='Teste',email='t@t.com',password='a2s3d4f5')
        data = {'username': w.username, 'email': w.email, 'password': w.password}
        form = UserForm(data=data)
        self.assertFalse(form.is_valid())
