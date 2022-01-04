from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name='despesas'),
    path('add-despesa',views.add_despesa,name='add-despesas'),


]