from django.urls import path

from conta.models import Conta
from . import views


urlpatterns = [
    #CONTAS
    path('contas', views.contas, name='contas'),
    path('add-conta', views.add_conta, name="add-conta"),
    path('edita-conta/<int:id>', views.editar_conta, name="edita-conta"),
    path('deletar-conta/<int:id>', views.deletar_conta, name='deletar-conta'),

    #DESPESAS
    path('', views.despesas, name="despesas"),
    path('add-expense', views.add_despesa, name="add-expenses"),
    path('add-categoria', views.add_tipodespesa, name='add-categoria'),
    path('edit-expense/<int:id>', views.editar_despesa, name="expense-edit"),
    path('expense-delete/<int:id>', views.deletar_despesa, name="expense-delete"),

    #RECEITAS
    path('receitas', views.receitas, name="receitas"),
    path('add-receita', views.add_receita, name="add-receita"),
    path('edita-receita/<int:id>', views.editar_receita, name="edita-receita"),
    path('deletar-receita/<int:id>', views.deletar_receita, name="deletar-receita")
    
]