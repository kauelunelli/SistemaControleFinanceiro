
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Receita, TipoDespesa, Despesa, Conta
# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
import datetime
from .filters import DespesaFilter


# CONTA

@login_required(login_url='/autenticacao/login')
def contas(request):
    contas = Conta.objects.all()
    paginator = Paginator(contas, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number) 
    context = {
        'contas': contas,
        'page_obj': page_obj,
    }
    return render(request, 'conta/contas.html', context)



@login_required(login_url='/autenticacao/login')
def add_conta(request):
    contas = Conta.objects.all()
    context = {
        'values': request.POST,
        'contas': contas,
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
        Conta.objects.create(dono=request.user,tipoConta=tipoConta, nome=nome, saldo=saldo, instituicao=instituicao)
        messages.success(request, 'Conta feita com Sucesso!')

        return redirect('add-conta')


@login_required(login_url='/autenticacao/login')
def editar_conta(request, id):
    contas = Conta.objects.get(pk=id)
    context = {
        'contas': contas,
        'values': request.POST,
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


def deletar_conta(request, id):
    conta = Conta.objects.get(pk=id)
    conta.delete()
    messages.success(request, 'Conta Excluida')
    return redirect('contas')



# DESPESA


@login_required(login_url='/autenticacao/login')
def despesas(request):
    despesas = Despesa.objects.filter(dono=request.user)
    paginator = Paginator(despesas, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number) 
    myFilter = DespesaFilter(request.GET, queryset=despesas)
    despesas = myFilter.qs
    context = {
        'despesas': despesas,
        'page_obj': page_obj,
        'myFilter': myFilter,
    }
    return render(request, 'despesas/despesas.html', context)


@login_required(login_url='/autenticacao/login')
def add_despesa(request):
    contas = Conta.objects.all()
    despesa = Despesa.objects.all()
    tipodespesa = TipoDespesa.objects.all()
    context = {
        'tipoDespesas': tipodespesa,
        'values': request.POST,
        'despesa': despesa,
        'contas' : contas,
    }
    if request.method == 'GET':
        return render(request, 'despesas/add-despesa.html', context)

    if request.method == 'POST':
        valor = request.POST['valor']

        if not valor:
            messages.error(request, 'Valor é necessário!')
            return render(request, 'despesas/add-despesa', context)
        descricao = request.POST['descricao']
        tipodespesa = request.POST['tipoDespesa']
        contas = request.POST['nome']
        dataPagamento = request.POST['dataPagamento']
        dataPagamentoEsperado = request.POST['dataPagamentoEsperado']

        if not descricao:
            messages.error(request, 'Descrição é necessario')
            return render(request, 'despesas/add-despesa', context)
        
        if not tipodespesa:
            messages.error(request, 'Precisa de uma Categoria!')
            return render(request, 'despesas/add-despesa', context)

        Despesa.objects.create(dono=request.user, valor=valor, descricao=descricao, dataPagamento=dataPagamento, dataPagamentoEsperado=dataPagamentoEsperado,
                               tipoDespesa=tipodespesa, conta=contas)
        messages.success(request, 'Expense saved successfully')

        return redirect('despesas')


@login_required(login_url='/autenticacao/login')
def editar_despesa(request, id):
    despesa = Despesa.objects.get(pk=id)
    tipoDespesas = TipoDespesa.objects.all()
    contas = Conta.objects.all()
    context = {
        'despesa': despesa,
        'values': despesa,
        'tipoDespesas': tipoDespesas,
        'contas' : contas
    }
    if request.method == 'GET':
        return render(request, 'despesas/edita-despesa.html', context)
    if request.method == 'POST':
        valor = request.POST['valor']

        if not valor:
            messages.error(request, 'Amount is required')
            return render(request, 'despesas/edita-despesa.html', context)

        descricao = request.POST['descricao']
        dataPagamento = request.POST['dataPagamento']
        dataPagamentoEsperado = request.POST['dataPagamentoEsperado']
        tipoDespesa = request.POST['tipoDespesa']
        contas = request.POST['conta']


        if not descricao:
            messages.error(request, 'description is required')
            return render(request, 'despesas/edita-despesa.html', context)

        despesa.dono = request.user
        despesa.valor = valor
        despesa.dataPagamento = dataPagamento
        despesa.dataPagamentoEsperado = dataPagamentoEsperado
        despesa.tipoDespesa = tipoDespesa
        despesa.descricao = descricao
        despesa.conta = contas

        despesa.save()
        messages.success(request, 'Despesa enviada com Sucesso!')

        return redirect('despesas')


def deletar_despesa(request, id):
    despesa = Despesa.objects.get(pk=id)
    despesa.delete()
    messages.success(request, 'Despesa Excluída')
    return redirect('despesas')

# RECEITA

@login_required(login_url='/autenticacao/login')
def receitas(request):
    receitas = Receita.objects.filter(dono=request.user)
    paginator = Paginator(receitas, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number) 
    context = {
        'receitas': receitas,
        'page_obj': page_obj,
    }
    return render(request, 'receitas/receitas.html', context)

@login_required(login_url='/autenticacao/login')
def add_receita(request):
    contas = Conta.objects.all()
    receita = Receita.objects.all()
    context = {
        'values': request.POST,
        'receita': receita,
        'contas' : contas,
    }
    if request.method == 'GET':
        return render(request, 'receitas/add-receita.html', context)

    if request.method == 'POST':
        valor = request.POST['valor']

        if not valor:
            messages.error(request, 'Precisa de um Valor!')
            return render(request, 'receitas/add-receita.html', context)
        descricao = request.POST['descricao']
        tiporeceita = request.POST['tipoReceita']
        contas = request.POST['nome']
        dataRecebimento = request.POST['dataRecebimento']
        dataRecebimentoEsperado = request.POST['dataRecebimentoEsperado']

        if not descricao:
            messages.error(request, 'description is required')
            return render(request, 'receitas/add-receita.html', context)
        
        if not tiporeceita:
            messages.error(request, 'Precisa de uma Categoria!')
            return render(request, 'receitas/add-receita.html', context)

        Receita.objects.create(dono=request.user, valor=valor, descricao=descricao, dataRecebimento=dataRecebimento, dataRecebimentoEsperado=dataRecebimentoEsperado,
                               tipoReceita=tiporeceita, conta=contas)
        messages.success(request, 'Receita salva com sucesso!')

        return redirect('receitas')

@login_required(login_url='/autenticacao/login')
def editar_receita(request, id):
    receita = Receita.objects.get(pk=id)
    contas = Conta.objects.all()
    context = {
        'receita': receita,
        'values': receita,
        'contas': contas,
    }
    if request.method == 'GET':
        return render(request, 'receitas/editar-receita.html', context)
    if request.method == 'POST':
        valor = request.POST['valor']

        if not valor:
            messages.error(request, 'Amount is required')
            return render(request, 'receitas/editar-receita.html', context)

        descricao = request.POST['descricao']
        dataRecebimento = request.POST['dataRecebimento']
        dataRecebimentoEsperado = request.POST['dataRecebimentoEsperado']
        tipoReceita = request.POST['tipoDespesa']
        contas = request.POST['conta']


        if not descricao:
            messages.error(request, 'description is required')
            return render(request, 'receitas/editar-receita.html', context)

        receita.dono = request.user
        receita.valor = valor
        receita.dataRecebimento = dataRecebimento
        receita.dataRecebimentoEsperado = dataRecebimentoEsperado
        receita.tipoReceita = tipoReceita
        receita.descricao = descricao
        receita.conta = contas

        receita.save()
        messages.success(request, 'Despesa enviada com Sucesso!')

        return redirect('receitas')

def deletar_receita(request, id):
    receita = Receita.objects.get(pk=id)
    receita.delete()
    messages.success(request, 'Receita Excluída')
    return redirect('receitas')

