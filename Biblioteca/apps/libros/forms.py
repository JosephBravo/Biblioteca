from django import forms
from apps.libros.models import Libro


class LibrosForm(forms.ModelForm):

	class Meta:
		model = Libro

		fields = [ 
			'id',
			'titulo',
			'subtitulo',
			'Autor',
			'fecha_publicacion',
			'editor',
			'descripcion',
			'imagen',	
		]

		labels = {
			'id': 'Id Numero Libro',
			'titulo': 'Titulo',
			'subtitulo': 'Subtitulo',
			'Autor': 'Autor',
			'fecha_publicacion': 'Fecha Publicacion',
			'editor': 'Editor',
			'descripcion': 'Descripción',
			'imagen': 'Imagen',
		}

		widgets = {
			'id': forms.TextInput(attrs={'class':'form-control'}),
			'titulo': forms.TextInput(attrs={'class':'form-control'}),
			'subtitulo': forms.TextInput(attrs={'class':'form-control'}),
			'Autor': forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),
			'fecha_publicacion': forms.DateInput(attrs={'class':'form-control'}),
			'editor': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'imagen': forms.TextInput(attrs={'class':'form-control'}),
		}