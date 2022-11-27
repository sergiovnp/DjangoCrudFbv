from django.shortcuts import render, get_object_or_404, redirect
from .models import Persona
from .forms import PersonaForm

# Create your views here.
def personaLista(request):
    personas = Persona.objects.all()
    return render (request, "lista.html", {'personas':personas} )


def personaDetalle(request, id):
    persona = get_object_or_404(Persona, pk=id)
    return render(request, "detalle.html", {'persona':persona})


def personaCrear(request):
    form = PersonaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista')
    
    return render(request, "crear.html", {'form':form})

