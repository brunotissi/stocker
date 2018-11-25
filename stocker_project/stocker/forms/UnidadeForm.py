from django import forms
from ..models import Unidade
from django.utils.translation import ugettext_lazy as _


class UnidadeForm(forms.ModelForm):
    nome = forms.CharField(label=_(u'Nome da Unidade de Medida'), required=True, widget=forms.TextInput
    (attrs={'placeholder': _(u'Nome da Unidade de Medida')}))

    class Meta:
        model = Unidade
        fields = ("nome",)

