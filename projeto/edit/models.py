from django.db import models


class edit(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    endereco = models.CharField(max_length=20, blank=False)
    telefone = models.CharField(max_length=100, blank=False)
    data_nascimento = models.DateField(blank=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.nome
