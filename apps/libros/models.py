
from django.core.files.images import ImageFile
from django.db import models


# Create your models here.


class Libro(models.Model):
	id = models.AutoField(primary_key = True)
	titulo = models.CharField(max_length=250)
	subtitulo= models.CharField(max_length=250)
	fecha_publicacion = models.DateField()
	editor = models.CharField(max_length=250)
	descripcion = models.CharField(max_length=250)
	imagen = models.ImageField(blank=True, null=True, upload_to = 'images')


	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name = 'Libro'
		verbose_name_plural = 'Libros'
		ordering = ["titulo"]


class Autor(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length=250)
	apellido= models.CharField(max_length=250)
	fecha_nacimiento = models.DateField()


	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name = 'Autor'
		verbose_name_plural = 'Autores'
		ordering = ["nombre"]


class Categoria(models.Model):
	id = models.AutoField(primary_key = True)
	nombre_categoria = models.CharField(max_length=250)


	def __str__(self):
		return self.nombre_categoria

	class Meta:
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'
		ordering = ["nombre_categoria"]
