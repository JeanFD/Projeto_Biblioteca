from django.contrib import admin

from .models import *

class UFInline(admin.TabularInline):
    model = UF
    extra = 1

class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

class AutorInline(admin.TabularInline):
    model = Autor
    extra = 1

class EditoraInline(admin.TabularInline):
    model = Editora
    extra = 1

class UsuarioInline(admin.TabularInline):
    model = Usuario
    extra = 1

class GeneroInline(admin.TabularInline):
    model = Genero
    extra = 1

class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1 # num de itens adicionais

class EmprestimoInline(admin.TabularInline):
    model = Emprestimo
    extra = 1


class UFAdmin(admin.ModelAdmin):
    list_display = ('sigla',)
    search_fields = ('sigla', ) 
    inlines = [CidadeInline]

class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome', ) 
    inlines = [AutorInline, UsuarioInline, EditoraInline]

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome', ) 
    inlines = [LivroInline]

class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome', ) 
    inlines = [LivroInline]

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome', ) 
    inlines = [EmprestimoInline]

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome', ) 
    inlines = [LivroInline]

class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome',) # campos exibidos
    search_fields = ('nome', ) # campos pesquisados
    inlines = [EmprestimoInline]





# admin.site.register(UFAdmin)
admin.site.register(UF, UFAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Editora, EditoraAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Livro, LivroAdmin)
admin.site.register(Emprestimo)
# Register your models here.
