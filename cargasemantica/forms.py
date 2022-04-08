from django import forms
from .models import Metadatos

class metadatosf(forms.ModelForm):

    passw = forms.CharField(max_length=25, label="Password", widget=forms.PasswordInput)

    class Meta:
        model = Metadatos
        fields = ['aliasconxion', 'comentariobd', 'nomhost', 'nompuerto', 'nombd', 'usuario', 'passw', 'fechacreacion']
	
		

	




