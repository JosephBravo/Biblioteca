from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.libros.forms import LibrosForm
from django.views.generic import TemplateView
from .models import Libro, Autor
	
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


class buscar_view(TemplateView):

		def post(self, request, *args, **kwargs):
			buscar = request.POST['buscalo']
			libros = Libro.objects.filter(titulo__contains=buscar)
			if libros:
				datos = []
				for libro in libros:
					autores = libro.Autor.all()
					datos.append(dict([(libro,autores)]))
					return render(request, 'buscar.html',
						{'datos':datos})
			else: 
				autores = Autor.objects.filter(nombre__contains=buscar)
			return render(request, 'buscar.html',
				{'autores':autores, 'autor':True}) 
			

"""def buscar_view(request):
	#template_name = 'buscar.html'
		return render(request, 'buscar.html') 
		buscar = request.POST['buscalo']
		
		def post(self, request, *args, **kwargs):
			return render(request, 'buscar.html') 
			print (buscalo)"""
	

