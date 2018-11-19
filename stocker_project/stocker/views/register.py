from django.shortcuts import render
from ..forms import UserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


def register(request):
	registered = False
	
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
	
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print(user_form.errors)
	
	else:
		user_form = UserForm()
	return render(request, 'stocker/register.html', {'user_form': user_form, 'registered': registered})


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Sua conta não é válida!")
		else:
			print("Campos inválidos: {0}, {1}".format(username, password))
			return HttpResponse("Campos inválidos!")
	else:
		return render(request, 'stocker/login.html', {})
