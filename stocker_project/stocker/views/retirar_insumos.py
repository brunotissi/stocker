from ..models import Insumo
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
#from .login_required import LoginRequiredMixin
from ..forms import EditInsumoForm
from ..models import Insumo


class retirar_insumos(View):
    form_class = EditInsumoForm
    initial = {}
    template_name = 'stocker/edit_insumos.html'

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

        if form_insumo.is_valid():
            insumo = form_insumo.save(commit=False)
            nova_quantidade = int(request.POST['quantidade'])

            quantidade_antiga = insumo.quantidade

            print(quantidade_antiga, 'oi')

            print(nova_quantidade, "______")
            if 'add-insumo' in request.POST:
                print(nova_quantidade, "+++++")
                qtd = quantidade_antiga + nova_quantidade
                print(qtd)
                # insumo.quantidade = nova_quantidade + insumo.quantidade
                insumo.save()

            elif 'remove-insumo' in request.POST:
                print(nova_quantidade, "----")
                insumo.quantidade = nova_quantidade - insumo.quantidade
                insumo.save()


            return HttpResponseRedirect(reverse('index'))
