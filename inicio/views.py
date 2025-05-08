from django.shortcuts import render
from .models import Aviso

def index(request):
    avisos = Aviso.objects.filter(ativo=True).order_by('data_publicacao')
    return render(request, 'inicio/index.html', {'avisos': avisos})
