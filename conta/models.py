from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.utils.timezone import now

# Create your models here.


class Receita(models.Model):
    valor = models.FloatField()
    dataRecebimento = models.DateField(default=now)
    dataRecebimentoEsperado = models.DateField(default=now)
    descricao = models.TextField()
    dono = models.ForeignKey(to=User, on_delete=models.CASCADE)
    conta = models.CharField(max_length=266)
    tipoReceita = models.CharField(max_length=266)

    def __str__(self):
        return self.conta

    class Meta:
        ordering: ['-date']





class Conta(models.Model):
    nome = models.CharField(max_length=255)
    dono = models.ForeignKey(to=User, on_delete=models.CASCADE)
    saldo = models.FloatField()
    instituicao = models.CharField(max_length=255)
    tipoConta = models.CharField(max_length=255)

    def __str__(self):
        return self.saldo



class Despesa(models.Model):
    valor = models.FloatField()
    dataPagamento = models.DateField(default=now)
    dataPagamentoEsperado = models.DateField(default=now)
    descricao = models.TextField()
    dono = models.ForeignKey(to=User, on_delete=models.CASCADE)
    conta = models.CharField(max_length=266)
    tipoDespesa = models.CharField(max_length=266)
    

    def __str__(self):
        return self.conta

    class Meta:
        ordering: ['-date']


class TipoDespesa(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'TipoDespesas'

    def __str__(self):
        return self.name
