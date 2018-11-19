from django.shortcuts import render
from ..models import Insumo


def retirar_insumos(request):
    lista_insumos = Insumo.objects.order_by('nome')
    context_dict = {'insumos': lista_insumos}
    return render(request, 'stocker/retirar_insumos.html', context_dict)