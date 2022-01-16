# DesafioPubFute

## Instalação

Siga os seguintes passos para instalar o projeto em sua máquina local.

1. Clone o repositório com: ``git clone https://github.com/kauelunelli/DesafioPubFuture``
2. Criar um ambiente virtual (python venv): ``python -m venv env``
3. Entre no ambiente virtual:
    - Para Linux:
      1. ``source ./env/bin/activate``
      
    - Para Windows:
      1. Se você não tiver feito anteriormente, entre no PowerShell como administrador e execute: ``**Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned**``
      2. execute: ``.\env\Scripts\Activate.ps1``
      
4.Todas as bibliotecas necessárias se encontram em 'requirements.txt', para instalar tudo de uma vez use `pip install -r requirements.txt`



5.Faça as migrações com: ``python manage.py migrate``

## Como Rodar

Após as migrações terem sido feitas você pode rodar a plataforma. Para rodar o servidor use ``python manage.py runserver``.
