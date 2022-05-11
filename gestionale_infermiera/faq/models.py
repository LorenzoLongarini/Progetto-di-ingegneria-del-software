from django.db import models

class FAQ(models.Model):

    nome = models.CharField(max_length=10)
    domanda = models.CharField(max_length=15)
    risposta = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
    
  