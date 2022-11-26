from django.shortcuts import render, get_object_or_404
from .models import Persona

# Create your views here.
def personaLista(request):
    personas = Persona.objects.all()
    return render (request, "lista.html", {'personas':personas} )


def personaDetalle(request, id):
    persona = get_object_or_404(Persona, pk=id)
    return render(request, "detalle.html", {'persona':persona})
