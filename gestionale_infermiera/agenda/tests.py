from django.test import TestCase
from agenda.models import Appuntamento

# Create your tests here.

class AppuntamentoTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Appuntamento.objects.create(id = 1, nome = "", day = "2022-05-31", orario_inizio = "18:00", orario_fine = "20:00", note = "")

    def test_nome_label(self):
        appuntamento = Appuntamento.objects.get(id=1)
        field_label = appuntamento._meta.get_field('nome').verbose_name
        self.assertEqual(field_label, 'Nome appuntamento')

    #FAIL
    def test_check_overlap(self):
        assert(Appuntamento.check_overlap(self, '18:00', '20:00', '14:00', '15:00',2))

    #FAIL
    def test_clean(self):
        appuntamento = Appuntamento.objects.create(id = 3, nome = "", day = "2022-05-31", orario_inizio = "18:00",
                                                     orario_fine = "15:00", note = "")
        assert(Appuntamento.clean(appuntamento))

    def test_get_absolute_url(self):
        appuntamento = Appuntamento.objects.get(id=1)
        self.assertEqual(appuntamento.get_absolute_url(), '<a href="/admin/agenda/appuntamento/1/change/">  18:00:00-20:00:00</a>')

