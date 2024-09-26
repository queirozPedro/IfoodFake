from django.db import models

class Item(models.Model):

    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    descricao = models.CharField(max_length=100)
    estabelecimento = models.CharField(max_length=100)
    observacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Pedido(models.Model):

    cliente = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    item = models.ManyToManyField(Item)
    valor_total = models.FloatField(default=0)
    data_cadastro = models.DateTimeField(auto_now=True)
    pago = models.BooleanField(default=False)
    