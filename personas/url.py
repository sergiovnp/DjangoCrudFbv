from django.urls import path
from . import views


urlpatterns = [
    path('', views.personaLista, name='lista'),
]
