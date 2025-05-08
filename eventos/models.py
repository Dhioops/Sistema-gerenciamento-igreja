from django.db import models
from membros.models import Membro

class CategoriaEvento(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    horario = models.TimeField()
    local = models.CharField(max_length=100)
    pregador = models.CharField(max_length=100, blank=True, null=True)
    categoria = models.ForeignKey(CategoriaEvento, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.nome} - {self.data}"

class Presenca(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)  # Removi o uso de string aqui
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE)
    data_presenca = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.membro.nome} - {self.evento.nome} ({self.data_presenca.strftime('%d/%m/%Y %H:%M')})"
