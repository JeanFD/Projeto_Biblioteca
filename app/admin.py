from django.contrib import admin

from .models import *

class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

class UFAdmin(admin.ModelAdmin):
    inlines = [CidadeInline]


admin.site.register(UF, UFAdmin)
admin.site.register(Cidade)
admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Leitor)
admin.site.register(Genero)
admin.site.register(Livro)
# Register your models here.
