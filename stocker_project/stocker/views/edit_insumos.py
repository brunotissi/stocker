from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from ..models import Insumo
from .login_required import LoginRequiredMixin


class edit_insumos(LoginRequiredMixin, View):
    initial = {}
    template_name = 'stocker/edit_insumos.html'

    def get(self, request, id=None, *args, **kwargs):
        insumo = Insumo.objects.get(pk=id)
        context_dict = {'insumo': insumo}

        return render(request, self.template_name, context_dict)

    def post(self, request, id=None, *args, **kwargs):
        insumo = Insumo.objects.get(pk=id)
        form_insumo = EditInsumoForm(instance=insumo, data=request.POST)
        qtd = int(request.POST['quantidade'])
        qtd2 = int(insumo.quantidade)
        qtd3 = qtd+qtd2
        qtd4 = qtd2-qtd
        if form_insumo.is_valid():
            if 'add-insumo' in request.POST:
                insumo.quantidade = qtd3
                insumo.save()
            elif 'remove-insumo' in request.POST:
                if qtd4 < 0:
                    insumo.quantidade = 0
                else:
                    insumo.quantidade = qtd4
                insumo.save()
            return HttpResponseRedirect(reverse('listar_insumos'))
