from django.contrib.auth import authenticate, get_user_model
from django import forms
from .models import Metadatos,Soporte

User = get_user_model()

class UsersLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput,)

	def __init__(self, *args, **kwargs):
		super(UsersLoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"username"})
		self.fields['password'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"password"})

	def clean(self, *args, **keyargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username = username, password = password)
			if not user:
				raise forms.ValidationError("Este usuario no existe")
			if not user.check_password(password):
				raise forms.ValidationError("Contraseña incorrecta")
			if not user.is_active:
				raise forms.ValidationError("El usuario no esta activo")

		return super(UsersLoginForm, self).clean(*args, **keyargs)


class metadatosf(forms.ModelForm):

    class Meta:
        model = Metadatos
        fields = ['aliasconxion', 'comentariobd', 'nomhost', 'nompuerto', 'nombd', 'usuario', 'passw', 'fechacreacion']
	
# aliasconxion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
# comentariobd = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
# nomhost = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
# nompuerto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
# nombd = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
# usuario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
# passw = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
# fechacreacion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

		
class soporte(forms.ModelForm):
	class Meta:
		model= Soporte
		fields = ['nombre', 'apellido', 'correo', 'detalleserror']
		#comentario por modificar 
	




