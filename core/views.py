from django.shortcuts import render
from .models import Parcela

def home(request):
    parcelas = Parcela.objects.all()
    return render(request, 'index.html', {'parcelas': parcelas})
