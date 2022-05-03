from django.db import models

class Prodotto(models.Model):

    nome = models.CharField(max_length=10)
    descrizione = models.CharField(max_length=30)
    marca = models.CharField(max_length=15)
    prezzo = models.FloatField(max_length=999)

    def __str__(self):
        return self.nome
    
  