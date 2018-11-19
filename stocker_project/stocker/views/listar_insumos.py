from ..models import Insumo
from django.shortcuts import render
from django.views.generic.base import View
from ..forms import UnidadeForm
#from .login_required import LoginRequiredMixin


class listar_insumos(View):
    form_class = UnidadeForm
    template_name = 'stocker/listar_insumos.html'

    def get(self, request, *args, **kwargs):
        insumos = Insumo.objects.all()
        return render(request, self.template_name, {'insumos': insumos})
