from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'livros.html')
    
class LivrosView(View):
    def get(self, request):
        contexto = {
            'livros': Livro.objects.all(),
            'emprestimo': Emprestimo.objects.all()
        }
        return render(request, 'livros.html', contexto)