from django.shortcuts import render
from .models import Persona

# Create your views here.
def personaLista(request):
    personas = Persona.objects.all()
    return render (request, "lista.html", {'personas':personas} )
