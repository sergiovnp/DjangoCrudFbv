from django.shortcuts import render, get_object_or_404, redirect
from .models import Persona
from .forms import PersonaForm

# Create your views here.
def personaLista(request):
    buscar = request.GET.get('buscar', None)

    if buscar:
        personas = Persona.objects.all()
        personas = personas.filter(apellido__icontains=buscar)
    else:
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

def personaEditar(request, id):
    persona = get_object_or_404(Persona, pk=id)
    form = PersonaForm(request.POST or None, instance=persona)

    if form.is_valid():
        form.save()
        return redirect('lista')

    return render(request, "editar.html", {'form':form})


def personaEliminar(request, id):
    persona = get_object_or_404(Persona, pk=id)

    if request.method == 'POST':
        persona.delete()
        return redirect('lista')

    return render(request, "eliminar.html", {'persona':persona})
