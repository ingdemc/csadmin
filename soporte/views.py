from django.shortcuts import render, redirect
from .forms import soporte

def soportes(request):
     if request.method == 'POST':
         form = soporte(request.POST)
         if form.is_valid():
            metadatos = form.save(commit=False)
            metadatos.author = request.user
            metadatos.save()
           
            return redirect('/soportes')
     else:
            form = soporte()
     return render(request, 'soporte.html', {'form': form})