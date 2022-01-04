from django.shortcuts import render
from django.views import View
# Create your views here.

class CadastroView(View):
    def get(self, request):
        return render(request, 'autenticacao/cadastro.html')