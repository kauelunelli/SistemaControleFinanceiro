from django_filters import DateFilter
import django_filters

from .models import Expense

class ExpenseFilter(django_filters.FilterSet):
    dataInicial = DateFilter(field_name='date', lookup_expr='gte')
    dataFinal = DateFilter(field_name='date', lookup_expr='lte')
    class Meta:
        model = Expense
        fields = '__all__'
        exclude = ['amount', 'owner', 'description', 'date']