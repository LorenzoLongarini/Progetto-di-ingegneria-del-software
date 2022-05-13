from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

min = 0
max = 999

def validate_price(value):
            if value < 0 :
                raise ValidationError(
                    _('Il prezzo non può essere negativo'),
                    params={'value': value},
                )

def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.nome) + "  " +str(self.orario_inizio) + "-"  +str(self.orario_fine) )

class Prodotto(models.Model):

    
    nome = models.CharField(u'Nome', help_text=u'Nome',max_length=10)
    descrizione = models.TextField(u'Descrizione', help_text=u'Descrizione', blank=True, null=True)
    marca = models.CharField(u'Marca', help_text=u'Marca',max_length=15, blank=True, null=True)
    prezzo = models.DecimalField(u'Prezzo', help_text=u'Prezzo', max_digits=5, validators=[validate_price], decimal_places=2)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = u'Prodotto'
        verbose_name_plural = u'Prodotti' 
    