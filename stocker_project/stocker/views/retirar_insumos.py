from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from ..forms import EditInsumoForm
from ..models import Insumo
from .login_required import LoginRequiredMixin


class retirar_insumos(LoginRequiredMixin, View):
    form_class = EditInsumoForm
    initial = {}
    template_name = 'stocker/retirar_insumos.html'

    def get(self, request, id=None, *args, **kwargs):
        insumo = Insumo.objects.get(pk=id)
        form_insumo = EditInsumoForm(instance=insumo)
        context_dict = {}
        context_dict['form'] = form_insumo
        context_dict['insumo'] = insumo
        return render(request, self.template_name, context_dict)

    def post(self, request, id=None, *args, **kwargs):
        insumo = Insumo.objects.get(pk=id)
        form_insumo = EditInsumoForm(instance=insumo, data=request.POST)
        qtd = int(request.POST['quantidade'])
        qtd2 = int(insumo.quantidade)
        qtd3 = qtd2-qtd
        if form_insumo.is_valid():
            if 'remove-insumo' in request.POST:
                if qtd3 < 0:
                    insumo.quantidade = 0
                else:
                    insumo.quantidade = qtd3
                insumo.save()

            return HttpResponseRedirect(reverse('listar_insumos'))
