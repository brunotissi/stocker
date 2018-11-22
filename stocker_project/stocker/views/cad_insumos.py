from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from ..forms import InsumoForm
from .login_required import LoginRequiredMixin
from .group_required import GroupRequiredMixin


class cad_insumos(GroupRequiredMixin, LoginRequiredMixin, View):
    group_required = 'gerentes'
    form_class = InsumoForm
    initial = {}
    template_name = 'stocker/cad_insumos.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('listar_insumos'))

        return render(request, self.template_name, {'form': form})
