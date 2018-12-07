from django.test import TestCase
from ..models import Unidade
from django.contrib.auth.models import User
from ..forms import UnidadeForm,UserForm,EditInsumoForm


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

class EditInsumoFormTest(TestCase):
    def test_valid_form(self):
        data = {'quantidade' : 100}
        form = EditInsumoForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'quantidade' : 'String'}
        form = UnidadeForm(data=data)
        self.assertFalse(form.is_valid())