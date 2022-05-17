from django.test import TestCase
from tariffa.models import Tariffa
from tariffa import models

# Create your tests here.

class TariffaTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tariffa.objects.create(nome = 'tariffa1', descrizione = "descrizione", prezzo= 9.99)

    def test_descrizione_label(self):
        tariffa = Tariffa.objects.get(id=1)
        field_label = tariffa._meta.get_field('descrizione').verbose_name
        self.assertEqual(field_label, 'Descrizione')

    def test_validate_price(self):
        tariffa = Tariffa.objects.get(id=1)
        prezzo = tariffa.prezzo
        assert(models.validate_price(prezzo),True)


    def test_descrizione_max_length(self):
        tariffa = Tariffa.objects.get(id=1)
        max_length = tariffa._meta.get_field('descrizione').max_length
        self.assertEqual(max_length, 300)

    #FAIL
    def test_get_absolute_url(self):
        tariffa = Tariffa.objects.get(id=1)
        self.assertEqual(tariffa.get_absolute_url(), 'href="/admin/prodotto/prodotto/1/change/')