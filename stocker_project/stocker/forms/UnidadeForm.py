from django import forms
from ..models import Unidade


class UnidadeForm(forms.ModelForm):
    nome = forms.CharField(label='Nome da Unidade de Medida', required=True, widget=forms.TextInput(attrs={'placeholder': 'Nome da Unidade de Medida'}))

    class Meta:
        model = Unidade
        fields = ("nome",)

