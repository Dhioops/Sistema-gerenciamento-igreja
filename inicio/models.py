from django.db import models

class Aviso(models.Model):
    titulo = models.CharField(max_length=100)
    mensagem = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
