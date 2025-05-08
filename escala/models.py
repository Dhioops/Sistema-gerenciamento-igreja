from django.db import models
from membros.models import Membro  # importar o seu modelo de membros

class EscalaCulto(models.Model):
    TIPO_CULTO_CHOICES = [
        ('Culto Divino', 'Culto Divino'),
        ('Culto Jovem', 'Culto Jovem'),
        ('Culto de Oração', 'Culto de Oração'),
        ('Culto de Gratidão', 'Culto de Gratidão'),
        ('Sábado Missionário', 'Sábado Missionário'),
        # adicione outros tipos se quiser
    ]

    data_culto = models.DateField()
    tipo_culto = models.CharField(max_length=30, choices=TIPO_CULTO_CHOICES)

    pregador = models.CharField(max_length=100, null=True, blank=True) # campo livre

    # agora usando o modelo Membro
    louvor = models.ForeignKey(Membro, on_delete=models.SET_NULL, null=True, related_name='louvor')
    historia_criancas = models.ForeignKey(Membro, on_delete=models.SET_NULL, null=True, related_name='historia_criancas')
    recepcao = models.ForeignKey(Membro, on_delete=models.SET_NULL, null=True, related_name='recepcao')
    media = models.ForeignKey(Membro, on_delete=models.SET_NULL, null=True, related_name='media')
    sonoplastia = models.ForeignKey(Membro, on_delete=models.SET_NULL, null=True, related_name='sonoplastia')

    def __str__(self):
        return f"{self.get_tipo_culto_display()} - {self.data_culto.strftime('%d/%m/%Y')}"

    class Meta:
        ordering = ['data_culto']
