from django.contrib import admin
from .models import Expense, Category, Receita, TipoConta, tipoReceita, conta
# Register your models here.


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'owner', 'category', 'date',)
    search_fields = ('description', 'category', 'date',)

    list_per_page = 5

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('valor', 'dataRecebimento', 'dataRecebimentoEsperado', 'descricao', 'dono', 'conta', 'tipoReceita')

    list_per_page = 5

class ContaAdmin(admin.ModelAdmin):
    list_display = ('saldo', 'instituicao')

admin.site.register(TipoConta)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Category)
admin.site.register(Receita, ReceitaAdmin)
admin.site.register(tipoReceita)
admin.site.register(conta)


