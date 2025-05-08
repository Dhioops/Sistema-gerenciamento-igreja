from django import forms
from .models import EscalaCulto
from membros.models import Membro

class EscalaCultoForm(forms.ModelForm):
    class Meta:
        model = EscalaCulto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Atualiza os campos para mostrar os nomes dos membros
        membros = Membro.objects.all()
        for campo in ['louvor', 'historia_criancas', 'recepcao', 'media', 'sonoplastia']:
            self.fields[campo].queryset = membros
            self.fields[campo].label_from_instance = lambda obj: obj.nome
