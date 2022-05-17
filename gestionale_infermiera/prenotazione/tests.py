from django.test import TestCase
from prenotazione.form import clean_data
from prenotazione.form import Prenotazione
from prenotazione import form

# Create your tests here.

class PrenotazioneTestCase(TestCase):

    def test_prescrizione_label(self):
        form = Prenotazione()
        self.assertTrue(form.fields['prescrizione'].label is None or 
            form.fields['prescrizione'].label == 'Possiedo la prescrizione del medico:')


    def test_prenotazionepage(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200) 

    #FAIL
    def test_clean_data(self):
        assert(form.clean_data('2022-01-24'))