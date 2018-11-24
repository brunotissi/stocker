from django.shortcuts import render
from django.contrib.auth import authenticate


def index(request):
	return render(request, 'stocker/index.html')

