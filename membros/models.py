# Create your models here.

from django.db import models
from django.contrib.auth.models import User  # Para associar o responsável a um usuário

class Membro(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

