import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Evento, Presenca  # Certifique-se de importar o modelo Presenca
from .forms import EventoForm

def lista_eventos(request):
    eventos = Evento.objects.all().order_by('data', 'horario')
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

def adicionar_evento(request):
    form = EventoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('eventos:lista_eventos')
    return render(request, 'eventos/adicionar_evento.html', {'form': form})

def editar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)  # Aqui alterei para usar 'id'
    form = EventoForm(request.POST or None, instance=evento)
    if form.is_valid():
        form.save()
        return redirect('eventos:lista_eventos')
    return render(request, 'eventos/editar_evento.html', {'form': form})

def excluir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)  # Aqui alterei para usar 'id'
    if request.method == 'POST':
        evento.delete()
        return redirect('eventos:lista_eventos')  # Corrigido o redirecionamento
    return render(request, 'eventos/confirmar_exclusao.html', {'evento': evento})

@login_required
def registrar_presenca(request, id):
    evento = get_object_or_404(Evento, id=id)  # Aqui alterei para usar 'id'

    if request.method == 'POST':
        # Verificar se o usuário está autenticado e associar o membro logado
        membro = request.user.membro  # Certifique-se de que o campo 'membro' existe no seu modelo User

        # Criar a presença
        presenca = Presenca(evento=evento, membro=membro)
        presenca.save()

        return redirect('eventos:lista_eventos')  # Redireciona para a lista de eventos após o registro

    return render(request, 'eventos/registrar_presenca.html', {'evento': evento})

def detalhes_evento(request, id):
    evento = get_object_or_404(Evento, id=id)  # Alterei para usar 'id'
    return render(request, 'eventos/detalhes_evento.html', {'evento': evento})
