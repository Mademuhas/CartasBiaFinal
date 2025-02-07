from django.db import models


class Objeto(models.Model):
    cont = models.PositiveIntegerField(default = 0)
    nome = models.CharField(max_length=55, null = True, blank = True, default = 'None' )
    src = models.CharField(max_length=55, null = True, blank = True, default = 'None' )
    def __str__(self):
        return self.nome
    

from django.db import models

class Escolha(models.Model):
    numero = models.IntegerField(default=0)
    nome = models.CharField(max_length=55, null=False)
    data = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return f'{self.nome}'