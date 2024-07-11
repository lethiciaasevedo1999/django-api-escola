from django.db import models

'''
Id
Nome
E-mail
Não pode estar em branco
CPF
Máximo de 11 caracteres
Data de Nascimento
'''

class Estudante(models.Model):
    nome = models.CharField(max_length= 100)
    email = models.EmailField(blank= False, max_length= 30)
    cpf = models.CharField(max_length= 11)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length= 14)

    def __str__(self):
        return self.nome
