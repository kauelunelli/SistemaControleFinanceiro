from django.urls import path

from conta.models import conta
from . import views


urlpatterns = [
    path('', views.despesas, name="despesas"),
    path('add-expense', views.add_expense, name="add-expenses"),
    path('add-categoria', views.add_categoria, name='add-categoria'),
    path('edit-expense/<int:id>', views.expense_edit, name="expense-edit"),
    path('expense-delete/<int:id>', views.delete_expense, name="expense-delete"),
    path('expense_category_summary', views.expense_category_summary,
         name="expense_category_summary"),
    path('stats', views.stats_view,
         name="stats"),
    path('add-conta', views.add_conta, name="add-conta"),
    path('contas', views.contas, name='contas'),
    path('edita-conta/<int:id>', views.editar_conta, name="edita-conta")
    
]