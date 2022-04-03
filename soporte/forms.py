from django import forms
from .models import Soporte


class soporte(forms.ModelForm):
	class Meta:
		model= Soporte
		fields = ['nombre', 'apellido', 'correo', 'detalleserror']
		#comentario por modificar 