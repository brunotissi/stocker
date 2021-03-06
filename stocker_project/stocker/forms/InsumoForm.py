from django import forms
from ..models import Insumo, Unidade
from django.utils.translation import ugettext_lazy as _

class InsumoForm(forms.ModelForm):
    nome = forms.CharField(label=_(u'Nome do Insumo'), required=True, widget=forms.TextInput(attrs={'placeholder': _(u'Nome do Insumo')}))
    quantidade = forms.IntegerField(label=_(u'Quantidade'), required=True, widget=forms.TextInput(attrs={'placeholder': _(u'Quantidade')}))
    unidade = forms.ModelChoiceField(label=_(u'Unidade de Medida'), required=True, queryset=Unidade.objects.all())

    def clean_quantidade(self):
        qtd = self.cleaned_data.get('quantidade')
        if int(qtd) < 0:
            raise forms.ValidationError("Quantidade deve ser maior ou igual a zero.")
        else:
            return qtd

    class Meta:
        model = Insumo
        fields = ('nome','quantidade', 'unidade', )


