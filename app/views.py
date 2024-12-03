from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
    
class PessoasFisicasView(View):
    def get(self, request):
        contexto = {
            'pessoasfisicas': PessoaFisica.objects.all(),
        }
        return render(request, 'pessoasfisicas.html', contexto)
    
class PessoasJuridicasView(View):
    def get(self, request):
        contexto = {
            'pessoasjuridicas': PessoaJuridica.objects.all(),
        }
        return render(request, 'pessoasjuridicas.html', contexto)
    
class AutoresView(View):
    def get(self, request):
        contexto = {
            'autores': Autor.objects.all(),
        }
        return render(request, 'autores.html', contexto)
    
class EditorasView(View):
    def get(self, request):
        contexto = {
            'editoras': Editora.objects.all(),
        }
        return render(request, 'editoras.html', contexto)

class UsuariosView(View):
    def get(self, request):
        contexto = {
            'usuarios': Usuario.objects.all(),
        }
        return render(request, 'usuarios.html', contexto)
    
class GenerosView(View):
    def get(self, request):
        contexto = {
            'generos': Genero.objects.all(),
        }
        return render(request, 'generos.html', contexto)
    
class AutoresView(View):
    def get(self, request):
        contexto = {
            'autores': Autor.objects.all(),
        }
        return render(request, 'autores.html', contexto)
    
class LivrosView(View):
    def get(self, request):
        contexto = {
            'livros': Livro.objects.all(),
            'emprestimo': Emprestimo.objects.all()
        }
        return render(request, 'livros.html', contexto)
    
class UfsView(View):
    def get(self, request):
        contexto = {
            'ufs': UF.objects.all(),
        }
        return render(request, 'ufs.html', contexto)
    
class CidadesView(View):
    def get(self, request):
        contexto = {
            'cidades': Cidade.objects.all(),
        }
        return render(request, 'cidades.html', contexto)
    
class EmprestimosView(View):
    def get(self, request):
        contexto = {
            'emprestimos': Emprestimo.objects.all(),
        }
        return render(request, 'emprestimos.html', contexto)