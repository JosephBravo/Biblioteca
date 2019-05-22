from django.contrib import admin

from apps.libros.models import Libro, Autor, Categoria

# Register your models here.
admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Categoria)