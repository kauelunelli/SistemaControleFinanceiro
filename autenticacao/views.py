from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
from .form import CreateUserForm


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('despesas')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Sua conta foi criada com sucesso!' + user)

				return redirect('login')
			else:
				messages.error(request, 'Erro ao criar sua conta.')

		context = {'form':form}
		return render(request, 'autenticacao/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('despesas')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('despesas')
			else:
				messages.info(request, 'Usuário ou Senha Incorreto')

		context = {}
		return render(request, 'autenticacao/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')
