from django import forms
from .models import Metadatos

class metadatosf(forms.ModelForm):

    class Meta:
        model = Metadatos
        fields = ['aliasconxion', 'comentariobd', 'nomhost', 'nompuerto', 'nombd', 'usuario', 'passw', 'fechacreacion']
	
		

	




