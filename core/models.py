from django.db import models
import datetime

data = datetime.date.today()

class FeriadosModel(models.Model):
    nome = models.CharField('Feriado',max_length=100)
    dia = models.IntegerField('Dia')
    mes = models.IntegerField('Mês')
    modificado_em = models.DateTimeField(verbose_name='modificado em',auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.nome