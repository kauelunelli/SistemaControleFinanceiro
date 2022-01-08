
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Expense, conta, TipoConta, tipoReceita
# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
import datetime
from .filters import ExpenseFilter


@login_required(login_url='/autenticacao/login')
def contas(request):
    contas = conta.objects.all()
    paginator = Paginator(contas, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number) 
    context = {
        'contas': contas,
        'page_obj': page_obj,
    }
    return render(request, 'conta/contas.html', context)

def add_conta(request):
    contas = conta.objects.all()
    TipoContas = TipoConta.objects.all()
    context = {
        'values': request.POST,
        'contas': contas,
        'TipoContas' : TipoContas,
    }
    if request.method == 'GET':
        return render(request, 'conta/add-conta.html', context)

    if request.method == 'POST':
        tipoConta = request.POST['tipoconta']
        nome = request.POST['nome']
        saldo = request.POST['saldo']
        instituicao = request.POST['instituicao']

        if not nome:
            messages.error(request, 'Precisa de um Nome sua Conta')
            return render(request, 'conta/add-conta.html')

        if not tipoConta:
            messages.error(request, 'Precisa de um estilo de Conta')
            return render(request, 'conta/add-conta.html', context)

        if not saldo:
            messages.error(request, 'saldo é necessario!')
            return render(request, 'conta/add-conta.html', context)
        
        if not instituicao:
            messages.error(request, 'Precisa de uma Instituição!')
        conta.objects.create(dono=request.user,tipoConta=tipoConta, nome=nome, saldo=saldo, instituicao=instituicao)
        messages.success(request, 'Conta feita com Sucesso!')

        return redirect('add-conta')

def editar_conta(request, id):
    contas = conta.objects.get(pk=id)
    TipoContas = TipoConta.objects.all()
    context = {
        'contas': contas,
        'values': request.POST,
        'TipoContas' : TipoContas,
    }
    if request.method == 'GET':
        return render(request, 'conta/editar-conta.html', context)
    if request.method == 'POST':
        nome = request.POST['nome']

        if not nome:
            messages.error(request, 'Precisa de um Nome!')
            return render(request, 'conta/editar-conta.html', context)
        saldo = request.POST['saldo']
        instituicao = request.POST['instituicao']
        tipoConta = request.POST['tipoconta']

        if not saldo:
            messages.error(request, 'Precisa de um Saldo')
            return render(request, 'conta/editar-conta.html', context)

        contas.dono = request.user
        contas.nome = nome
        contas.saldo = saldo
        contas.instituicao = instituicao
        contas.tipoConta = tipoConta

        contas.save()
        messages.success(request, 'Conta enviada com Sucesso!')

        return redirect('contas')





@login_required(login_url='/autenticacao/login')
def despesas(request):
    categories = Category.objects.all()
    expenses = Expense.objects.filter(owner=request.user)
    paginator = Paginator(expenses, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number) 
    myFilter = ExpenseFilter(request.GET, queryset=expenses)
    expenses = myFilter.qs
    context = {
        'expenses': expenses,
        'page_obj': page_obj,
        'myFilter': myFilter,
    }
    return render(request, 'expenses/despesas.html', context)


def add_expense(request):
    contas = conta.objects.all()
    expense = Expense.objects.all()
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'values': request.POST,
        'expense': expense,
        'contas' : contas,
    }
    if request.method == 'GET':
        return render(request, 'expenses/add_expense.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'expenses/add_expense.html', context)
        description = request.POST['description']
        date = request.POST['expense_date']
        category = request.POST['category']
        contas = request.POST['nome']

        if not description:
            messages.error(request, 'description is required')
            return render(request, 'expenses/add_expense.html', context)

        Expense.objects.create(owner=request.user, amount=amount, date=date,
                               category=category, description=description, contas=contas)
        messages.success(request, 'Expense saved successfully')

        return redirect('despesas')

def add_categoria(request):
    categoria = Category.objects.all()
    context = {
        'categoria' : categoria,
    }
    if request.method == 'GET':
        return render(request, 'expenses/add-categoria.html', context)

    if request.method == 'POST':
        categoria = request.POST['categoria']

    if not categoria:
        messages.error(request, "Precisa de uma Categoria")
        return render(request, 'expense/add-categoria.html', context)

    Category.objects.create(name=categoria)
    messages.success(request, 'Categoria salva com sucesso!')

    return redirect('add-expenses')



def expense_edit(request, id):
    expense = Expense.objects.get(pk=id)
    categories = Category.objects.all()
    context = {
        'expense': expense,
        'values': expense,
        'categories': categories
    }
    if request.method == 'GET':
        return render(request, 'expenses/edit-expense.html', context)
    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'expenses/edit-expense.html', context)
        description = request.POST['description']
        date = request.POST['expense_date']
        category = request.POST['category']

        if not description:
            messages.error(request, 'description is required')
            return render(request, 'expenses/edit-expense.html', context)

        expense.owner = request.user
        expense.amount = amount
        expense. date = date
        expense.category = category
        expense.description = description

        expense.save()
        messages.success(request, 'Despesa enviada com Sucesso!')

        return redirect('despesas')


def delete_expense(request, id):
    expense = Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request, 'Despesa Excluída')
    return redirect('despesas')


def expense_category_summary(request):
    todays_date = datetime.date.today()
    six_months_ago = todays_date-datetime.timedelta(days=30*6)
    expenses = Expense.objects.filter(owner=request.user,
                                      date__gte=six_months_ago, date__lte=todays_date)
    finalrep = {}

    def get_category(expense):
        return expense.category
    category_list = list(set(map(get_category, expenses)))

    def get_expense_category_amount(category):
        amount = 0
        filtered_by_category = expenses.filter(category=category)

        for item in filtered_by_category:
            amount += item.amount
        return amount

    for x in expenses:
        for y in category_list:
            finalrep[y] = get_expense_category_amount(y)

    return JsonResponse({'expense_category_data': finalrep}, safe=False)


def stats_view(request):
    return render(request, 'expenses/stats.html')
