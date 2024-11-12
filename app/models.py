from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, default='')
    email = models.CharField(default = '')
    telefone = models.CharField(default = 0)
    cidade = models.ForeignKey("Cidade", on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        abstract = True
    def __str__(self):
        return self.nome
    

class PessoaFisica(Pessoa):
    cpf = models.IntegerField(default = 0)
    data_nasc = models.DateField(default = '2000-01-01', verbose_name="Data de Nascimento") # yyyy-mm-dd
    class Meta:
        abstract = True
    def __str__(self):
        return self.nome


class PessoaJuridica(Pessoa):
    cnpj = models.IntegerField(default = 0)
    razao_social = models.CharField(default = '', verbose_name='Razão Social')
    class Meta:
        abstract = True
    def __str__(self):
        return self.razao_social
  
  
class Autor(PessoaFisica):
    pass
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


class Editora(PessoaJuridica):
    site = models.CharField(max_length=100, verbose_name='Site da editora')
    class Meta:
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"


class Usuario(PessoaFisica):
    pass
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class Genero(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Genero')
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"


class Livro(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do livro')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name='Autor do livro')
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, verbose_name='Editora do livro')
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name='Gênero do livro')
    preco = models.IntegerField(verbose_name='Preço do livro')
    data_plub = models.DateField(verbose_name='Data de publicação do livro')
    status = models.BooleanField(verbose_name='Status do livro')

    def __str__(self):
        return f'{self.nome}, {self.autor}'
    
    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"


class UF(models.Model):
    sigla = models.CharField(max_length=2)

    class Meta:
        verbose_name = "Unidade Federal"
        verbose_name_plural = "Unidades Federais"

    def __str__(self):
        return self.sigla


class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da cidade')
    uf = models.ForeignKey(UF, on_delete=models.CASCADE, verbose_name='UF')
    def __str__(self):
        return f'{self.nome}, {self.uf}'
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Emprestimo(models.Model):
    data_emp = models.DateField(verbose_name='Data de Emprestimo')
    livro_emp = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name='livro emprestado')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario que pegou o livro')
    def __str__(self):
        return f'{self.livro_emp}, {self.livro_emp}, {self.usuario}'
    class Meta:
        verbose_name = "Emprestimo"
        verbose_name_plural = "Emprestimos"