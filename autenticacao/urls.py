from django.urls import path
from . import views
from .views import CadastroView

urlpatterns = [
    path('cadastro', CadastroView.as_view(), name='cadastro')
]