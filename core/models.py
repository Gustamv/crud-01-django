from django.db import models

#eh como cria dados no bd
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)

#para que o nome seja impresso de forma mais simples no bd ao inves de Pessoa object
    def __str__(self):
        return self.nome
        #estudar self