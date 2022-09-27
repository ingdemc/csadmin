from django import forms
from .models import Metadatos,schema_gr


class metadatosf(forms.ModelForm):

    
    
    passw = forms.CharField(max_length=150, label="Password", widget=forms.PasswordInput)
    

    class Meta:
        model = Metadatos
        fields = ['aliasconxion', 'comentariobd', 'nomhost', 'nompuerto', 'nombd', 'usuario', 'passw']
        labels = {'aliasconxion':('Alias de conexion '),
        'comentariobd':('Comentario '),
        'nomhost':('Nombre host'),
        'nompuerto':(' Numero de puerto'),
        'nombd':(' Nombre de la base de datos'),
        'usuario':('Nombre de usuario'),
        'passw':('Contraseña')}
		

class diag(forms.ModelForm):

    class Meta:
        model=schema_gr
        fields =['id_schema','image']
 
	




