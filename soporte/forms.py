from django import forms
from .models import Soporte
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Soporte(forms.ModelForm):
	class Meta:
		model= Soporte
		fields = ['nombre', 'apellido', 'correo', 'detalleserror']
		#comentario por modificar 
		
		


class CustomCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields =['username','first_name','last_name',"email","password1","password2"]