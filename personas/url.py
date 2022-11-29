from django.urls import path
from . import views


urlpatterns = [
    path('', views.personaLista, name='lista'),
    path('detalle/<int:id>/', views.personaDetalle, name='detalle'),
    path('crear/', views.personaCrear, name='crear'),
    path('editar/<int:id>/', views.personaEditar, name='editar',)
]
