from django.test import TestCase
from fattura.models import Fattura
from fattura.models import TariffaFatt
from fattura import models

# Create your tests here.

class FatturaTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Fattura.objects.create(id=1, nome="Mario", cognome="Rossi", nome_ditta="", citta="Macerata", via="Rossini", num_civico=8,
                               cap=62100, partita_iva=1111, cod_fiscale="BBBBB7865YFYF", cod_cliente="1234567", numero=1, 
                               data = "2022-05-31", descrizione_pag = "descrizione", banca = "IT00000123")
        TariffaFatt.objects.create(descrizione_prod="descrizione1", quantita=3, prezzo=10.50, fatt=Fattura.objects.get(id=1))

    #FAIL
    def test_cod_cliente_label(self):
        fattura = Fattura.objects.get(id=1)
        field_label = fattura._meta.get_field('cod_cliente').verbose_name
        self.assertEqual(field_label, 'cod_cliente')

    def test_quantita_label(self):
        fatt_prod = TariffaFatt.objects.get(id=1)
        field_label = fatt_prod._meta.get_field('quantita').verbose_name
        self.assertEqual(field_label, 'Quantità')

    def test_cod_fiscale(self):
        fattura = Fattura.objects.get(id=1)
        max_length = fattura._meta.get_field('cod_fiscale').max_length
        self.assertEqual(max_length, 16)

    def test_validate_price(self):
        fattura = Fattura.objects.get(id=1)
        prezzo = fattura.prezzo
        assert(models.validate_price(prezzo),True)
