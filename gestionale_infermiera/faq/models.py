from django.db import models

class FAQ(models.Model):

    nome = models.CharField(max_length=50)
    domanda = models.CharField(max_length=100)
    risposta = models.CharField(max_length=500)

    def __str__(self):
        return self.nome
    
  