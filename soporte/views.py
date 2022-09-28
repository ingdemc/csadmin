from django.shortcuts import render, redirect
from cargasemantica.forms import Metadatos
from soporte.forms import CustomCreationForm
from django.contrib.auth import login, logout,authenticate
from .forms import Soporte
from.models import soporte

def soportes(request):
     form= soporte()
     if request.method == 'POST':
         form = soporte(request.POST)
         if form.is_valid():
            metadatos = form.save(commit=False)
            metadatos.iduser = request.user
            metadatos.save()
           
            return redirect('/soportes')
     else:
            form = soporte()
     return render(request, 'soporte.html', {'form': form})

# Create your views here.
def pgprincipal(request):
	id= request.user.id
	msgsoporte= Soporte.objects.filter(iduser=id)
	numero_reg=Soporte.objects.filter(iduser=id).count()
	met_reg= Metadatos.objects.filter(iduser=id).count()
	# sql1 =('''SELECT COUNT(*) FROM cargasemantica_metadatos''')

	return render(request, "pgprincipal.html", {'msgsoporte':msgsoporte,'numero_reg':numero_reg,'met_reg':met_reg})
	
# def logout_user(request):
# 	logout(request)
# 	return redirect('/register')


def RegistrarUsuario(request):
	data={
		'form':CustomCreationForm()
	}

	if request.method == 'POST':
		formulario = CustomCreationForm(data= request.POST)
		if formulario.is_valid():
			formulario.save()
			user=authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
			login(request,user)

			return redirect(to="pg")
		data["form"]= formulario
	return render(request, "register.html",data)
	



