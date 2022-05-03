from django.db import models

class Tariffa(models.Model):

    nome = models.CharField(max_length=10)
    descrizione = models.CharField(max_length=30, default=None, blank=True, null=True)
    prezzo = models.FloatField(max_length=999)

    def __str__(self):
        return self.nome
    
  