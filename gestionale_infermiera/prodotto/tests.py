from django.test import TestCase
from prodotto.models import Prodotto

# Create your tests here.

class ProdottoTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Prodotto.objects.create(nome = 'esempio1', domanda = "domanda1", risposta= "risposta1")

    def test_nome_label(self):
        prodotto = Prodotto.objects.get(id=1)
        field_label = prodotto._meta.get_field('nome').verbose_name
        self.assertEqual(field_label, 'nome')