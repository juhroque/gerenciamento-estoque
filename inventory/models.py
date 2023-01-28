from django.db import models

class Inventory(models.Model):

    opcoes_categoria = [
        ('ELETRODOMÉSTICOS', 'Eletrodomésticos'),
        ('ELETRÔNICOS','Eletrônicos')
    ]

    nome = models.CharField(max_length=150, null=False, blank=False)
    preco = models.FloatField(null=False, blank=False)
    quantidade = models.IntegerField(null=False, blank=False)
    categoria = models.CharField(max_length=100, choices = opcoes_categoria, default ='')

    def __str__(self):
        return self.nome