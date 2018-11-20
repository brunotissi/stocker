from django import forms
from django.contrib.auth.models import User
from .models import Insumo, Unidade


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')


class InsumoForm(forms.ModelForm):
	nome = forms.CharField(label='Nome do Insumo', required=True, widget=forms.TextInput(attrs={'placeholder': 'Nome do Insumo'}))
	quantidade = forms.IntegerField(label='Quantidade', required=True, widget=forms.TextInput(attrs={'placeholder': 'Quantidade'}))
	unidade = forms.ModelChoiceField(label='Unidade de Medida', required=True, queryset=Unidade.objects.all())

	class Meta:
		model = Insumo
		fields = ('nome','quantidade', 'unidade', )


class EditInsumoForm(forms.ModelForm):
	class Meta:
		model = Insumo
		fields = ('quantidade',)


class UnidadeForm(forms.ModelForm):
	nome = forms.CharField(label='Nome da Unidade de Medida', required=True, widget=forms.TextInput(attrs={'placeholder': 'Nome da Unidade de Medida'}))

	class Meta:
		model = Unidade
		fields = ("nome",)
