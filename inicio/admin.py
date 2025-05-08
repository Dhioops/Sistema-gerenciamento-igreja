# admin.py do app 'inicio'
from django.contrib import admin
from .models import Aviso

@admin.register(Aviso)
class AvisoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ativo', 'data_publicacao')  # Alterado de 'criado_em' para 'data_publicacao'
    list_filter = ('ativo', 'data_publicacao')  # Alterado de 'criado_em' para 'data_publicacao'
    search_fields = ('titulo', 'mensagem')
