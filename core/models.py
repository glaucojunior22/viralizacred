from django.db import models


class Parcela(models.Model):
    banco = models.CharField(max_length=255)
    tipo = models.IntegerField()
    posto = models.CharField(max_length=2)
    nome = models.CharField(max_length=255)
    numero_ordem = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)
    upag = models.CharField(max_length=50)
    sub_om = models.CharField(max_length=10)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    prazo = models.DateField()

    def __str__(self):
        return self.nome