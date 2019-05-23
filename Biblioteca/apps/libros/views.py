from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.libros.forms import LibrosForm

from django.views.generic import TemplateView
	
# Create your views here.

def index(request):
	return render(request, 'index.html')


def libros_view(request):
	if request.method == 'POST':
		form = LibrosForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index')
	else:
		form = LibrosForm()
	return render(request, 'formulario.html', {'form':form})


def buscar_view(request):
	#template_name = 'buscar.html'
		return render(request, 'buscar.html') 
		buscar = request.POST['buscalo']
		
		if post(self, request, *args, **kwargs):
			return render(request, 'buscar.html') 
			print (buscar)
	

