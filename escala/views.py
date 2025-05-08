from django.shortcuts import render, get_object_or_404, redirect
from .models import EscalaCulto
from .forms import EscalaCultoForm
from django.contrib import messages
from django.http import JsonResponse
from .models import Membro

# Página para listar escalas de culto
def listar_escala(request):
    escalas = EscalaCulto.objects.all()
    return render(request, 'escala/lista_escala.html', {'escalas': escalas})

# Página para adicionar uma nova escala de culto
def adicionar_escala(request):
    if request.method == 'POST':
        form = EscalaCultoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Escala de culto adicionada com sucesso!")
            return redirect('listar_escala')
        else:
            messages.error(request, "Erro ao adicionar a escala. Verifique os dados.")
    else:
        form = EscalaCultoForm()
    return render(request, 'escala/adicionar_escala.html', {'form': form})

# Página para editar uma escala de culto
def editar_escala(request, pk):
    escala = get_object_or_404(EscalaCulto, pk=pk)
    if request.method == 'POST':
        form = EscalaCultoForm(request.POST, instance=escala)
        if form.is_valid():
            form.save()
            messages.success(request, "Escala de culto editada com sucesso!")
            return redirect('listar_escala')
        else:
            messages.error(request, "Erro ao editar a escala. Verifique os dados.")
    else:
        form = EscalaCultoForm(instance=escala)
    return render(request, 'escala/editar_escala.html', {'form': form})

# Página para excluir uma escala de culto
def excluir_escala(request, pk):
    escala = get_object_or_404(EscalaCulto, pk=pk)
    if request.method == 'POST':
        escala.delete()
        messages.success(request, "Escala de culto excluída com sucesso!")
        return redirect('listar_escala')
    return render(request, 'escala/confirmar_exclusao_escala.html', {'escala': escala})

from django.http import JsonResponse
from membros.models import Membro  # ou o nome correto do seu app/modelo

def autocomplete_membros(request):
    if 'term' in request.GET:
        qs = Membro.objects.filter(nome__icontains=request.GET.get('term'))
        nomes = list(qs.values_list('nome', flat=True))
        return JsonResponse(nomes, safe=False)
    return JsonResponse([], safe=False)

def buscar_membros(request):
    termo = request.GET.get('q', '')
    membros = Membro.objects.filter(nome__icontains=termo)
    resultados = [{'id': m.id, 'text': m.nome} for m in membros]
    return JsonResponse({'results': resultados})
