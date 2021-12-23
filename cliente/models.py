from django.db import models

class cliente(models.Model):
    nome = models.CharField(max_length=80, blank=False)
    cpf = models.CharField(max_length=11, blank=False)
    data_nascimento = models.DateField(blank=False)
    telefone = models.CharField(max_length=11, blank=False)

    def __str__(self) -> str:
        return self.nome