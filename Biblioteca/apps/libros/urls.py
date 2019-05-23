from django.urls import path
from . import views
from apps.libros.views import index, libros_view, buscar_view

urlpatterns = [
    path('', views.index, name='index'),
    path('nuevo', libros_view, name='libro_nuevo'),
    path('buscar', buscar_view, name='buscar')
      ]