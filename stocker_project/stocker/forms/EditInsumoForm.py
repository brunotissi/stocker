from django import forms
from ..models import Insumo
from django.utils.translation import ugettext_lazy as _

class EditInsumoForm(forms.ModelForm):
    quantidade = forms.IntegerField(label=_(u'Quantidade atual'))


    class Meta:
        model = Insumo
        fields = ('quantidade',)
