from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'despesas/inicio.html')

def add_despesa(request):
    return render(request, 'despesas/add_despesa.html')
    
