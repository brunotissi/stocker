from django import forms
from django.contrib.auth.models import User
from .models import Insumo, Unidade


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password')


class InsumoForm(forms.ModelForm):
	class Meta:
		model = Insumo
		fields = ('nome', 'quantidade', 'unidade', )

class UnidadeForm(forms.ModelForm):
	class Meta:
		model = Unidade
		fields = ("nome",)
