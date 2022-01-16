from django.contrib import admin
from .models import Despesa, TipoDespesa, Receita, Conta
# Register your models here.


class DespesaAdmin(admin.ModelAdmin):
    list_display = ('conta', 'tipoDespesa')



class ContaAdmin(admin.ModelAdmin):
    list_display = ('saldo', 'instituicao')


admin.site.register(Despesa, DespesaAdmin)
admin.site.register(TipoDespesa)
admin.site.register(Receita)

admin.site.register(Conta, ContaAdmin)


