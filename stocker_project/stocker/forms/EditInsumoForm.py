from django import forms
from ..models import Insumo


class EditInsumoForm(forms.ModelForm):
    quantidade = forms.IntegerField(label='Quantidade atual')
    class Meta:
        model = Insumo
        fields = ('quantidade',)
