from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UsersLoginForm,RegisterForm
from soporte.forms import Soporte
from django.contrib.auth.decorators import login_required

def login_view(request):
	form = UsersLoginForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		user = authenticate(email = email, password = password)
		login(request, user)
		return redirect("/")
		

	return render(request, "accounts/login.html", {
		"form" : form,
		"title" : "Login",
	})

def pgprincipal(request):
	msgsoporte= Soporte.objects.all()
	return render(request, "pgprincipal.html", {'msgsoporte':msgsoporte})


def register(request):
	register_form= RegisterForm()
	if request.method == 'POST':
		register_form= RegisterForm(request.POST)
		
		if register_form.is_valid():
			register_form.save()
			messages.success(request,'te has registrado correctamente')

			return redirect('/accounts/login')
	return render(request, 'register.html', {
		'title' : 'Register',
		'register_form': register_form
	})

def logout_user(request):
	logout(request)
	return redirect('/register')