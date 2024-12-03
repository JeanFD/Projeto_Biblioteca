from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('pessoasfisicas/', PessoasFisicasView.as_view(), name='pessoasfisicas'),
    path('pessoasjuridicas/', PessoasJuridicasView.as_view(), name='pessoasjuridicas'),
    path('autores/', AutoresView.as_view(), name='autores'),
    path('editoras/', EditorasView.as_view(), name='editoras'),
    path('usuarios/', UsuariosView.as_view(), name='usuarios'),
    path('generos/', GenerosView.as_view(), name='generos'),
    path('livros/', LivrosView.as_view(), name='livros'),
    path('ufs/', UfsView.as_view(), name='ufs'),
    path('cidades/', CidadesView.as_view(), name='cidades'),
    path('emprestimos/', EmprestimosView.as_view(), name='emprestimos')
]