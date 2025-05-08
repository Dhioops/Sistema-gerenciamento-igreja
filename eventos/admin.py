from django.contrib import admin
from .models import Evento, CategoriaEvento, Presenca

admin.site.register(Evento)
admin.site.register(CategoriaEvento)

class PresencaAdmin(admin.ModelAdmin):
    list_display = ('evento', 'membro', 'data_presenca')
    search_fields = ('evento__nome', 'membro__nome')

admin.site.register(Presenca, PresencaAdmin)