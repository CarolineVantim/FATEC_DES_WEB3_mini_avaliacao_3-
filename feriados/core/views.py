from django.shortcuts import render
import datetime

data = datetime.date.today()

def natal(request):
    if data.month == 12 and data.day == 25:
        contexto = {
            'natal': True
        }
        return render(request, 'natal.html', contexto)
    else:
        contexto = {
            'natal': False
        }
        return render(request, 'natal.html', contexto)

def tiradentes(request):
    if data.month == 4 and data.day == 21:
        condicao = {
            'tiradentes': True
        }
        return render(request, 'tiradentes.html', condicao)
    else:
        contexto = {
            'tiradentes': False
        }
        return render(request, 'tiradentes.html', condicao)