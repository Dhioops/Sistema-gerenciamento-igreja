from django import forms
from .models import Membro


class MembroForm(forms.ModelForm):
    class Meta:
        model = Membro
        fields = ['nome', 'email', 'telefone']  # inclua aqui os campos que você definiu no model

