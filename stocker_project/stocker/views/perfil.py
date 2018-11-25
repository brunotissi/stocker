from django.shortcuts import render
from django.views.generic.base import View
from .login_required import LoginRequiredMixin
from django.contrib.auth.models import User


class Perfil(LoginRequiredMixin, View):
    template_name = 'stocker/perfil.html'

    def get(self, request, *args, **kwargs):
        user = request.user.id
        print("-----", user)
        pessoa = User.objects.get(id=user)
        print("-----", pessoa.username)
        return render(request, self.template_name, {'pessoa': pessoa})