from django import forms
from ..models import Insumo, Unidade


class InsumoForm(forms.ModelForm):
    nome = forms.CharField(label='Nome do Insumo', required=True, widget=forms.TextInput(attrs={'placeholder': 'Nome do Insumo'}))
    quantidade = forms.IntegerField(label='Quantidade', required=True, widget=forms.TextInput(attrs={'placeholder': 'Quantidade'}))
    unidade = forms.ModelChoiceField(label='Unidade de Medida', required=True, queryset=Unidade.objects.all())

    class Meta:
        model = Insumo
        fields = ('nome','quantidade', 'unidade', )


