from django.test import TestCase
from prodotto.models import Prodotto
from prodotto import models

# Create your tests here.

class ProdottoTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Prodotto.objects.create(nome = 'prodotto1', descrizione = "descrizione generica", marca= "marca1", prezzo = -3)

    #FAIL
    def test_marca_label(self):
        prodotto = Prodotto.objects.get(id=1)
        field_label = prodotto._meta.get_field('marca').verbose_name
        self.assertEqual(field_label, 'marca')

    def test_validate_price(self):
        prodotto = Prodotto.objects.get(id=1)
        prezzo = prodotto.prezzo
        assert(models.validate_price(prezzo),False)

    def test_get_absolute_url(self):
        prodotto = Prodotto.objects.get(id=1)
        self.assertEqual(prodotto.get_absolute_url(), '<a href="/admin/prodotto/prodotto/1/change/">prodotto1</a>')