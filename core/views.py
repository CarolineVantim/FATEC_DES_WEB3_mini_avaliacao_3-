from django.shortcuts import render
from .models import FeriadosModel
import datetime

data = datetime.date.today()
qs = FeriadosModel.objects.all()

def feriado(request):
    for f in qs:
        if f.dia == data.day and f.mes == data.month:
            contexto = {
                'nome': f.nome
            }
            return render(request, 'index.html', contexto)
    else:
        contexto = {
            'nome': False
        }
        return render(request, 'index.html', contexto)