from django_filters import DateFilter
import django_filters

from .models import Despesa, Conta

class DespesaFilter(django_filters.FilterSet):
    dataInicial = DateFilter(field_name='dataPagamento', lookup_expr='gte')
    dataFinal = DateFilter(field_name='dataPagamento', lookup_expr='lte')
    class Meta:
        model = Despesa
        fields = '__all__'
        exclude = ['valor', 'dono', 'descricao', 'dataPagamento']

