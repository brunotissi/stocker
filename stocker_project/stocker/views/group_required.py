from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class GroupRequiredMixin(object):
    group_required = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('listar_insumos'), {'mensagem': 'Você não tem permissão para acessar essa página.'})
        else:
            user_groups = []
            for group in request.user.groups.values_list('name', flat=True):
                user_groups.append(group)
            if len(set(user_groups).intersection(self.group_required)) <= 0:
                return HttpResponseRedirect(reverse('listar_insumos'), {'mensagem': 'Você não tem permissão para acessar essa página.'})
        return super(GroupRequiredMixin, self).dispatch(request, *args, **kwargs)