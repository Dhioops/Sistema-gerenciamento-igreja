from django.shortcuts import render, get_object_or_404, redirect
from .models import Membro
from .forms import MembroForm

# Página inicial
def index(request):
    return render(request, 'membros/index.html')  # Sem 'templates/', já que o Django já está configurado para procurar nessa pasta

# Lista de membros
def lista_membros(request):
    membros = Membro.objects.all()
    return render(request, 'membros/lista_membros.html', {'membros': membros})

# Adicionar Membro
def adicionar_membro(request):
    if request.method == 'POST':
        form = MembroForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo membro no banco de dados
            return redirect('lista_membros')  # Redireciona para a lista de membros após salvar
    else:
        form = MembroForm()  # Cria um formulário vazio para ser preenchido

    return render(request, 'membros/adicionar_membro.html', {'form': form})  # Renderiza o template com o formulário

# Editar Membro
def editar_membro(request, id):
    membro = get_object_or_404(Membro, id=id)
    
    if request.method == 'POST':
        form = MembroForm(request.POST, instance=membro)
        if form.is_valid():
            form.save()
            return redirect('lista_membros')
    else:
        form = MembroForm(instance=membro)
    
    return render(request, 'membros/editar_membro.html', {'form': form})

# Excluir Membro
def excluir_membro(request, id):
    membro = get_object_or_404(Membro, id=id)
    
    if request.method == 'POST':
        membro.delete()
        return redirect('lista_membros')
    
    return render(request, 'membros/confirmar_exclusao.html', {'membro': membro})
