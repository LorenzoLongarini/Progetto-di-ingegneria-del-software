# -*- coding: utf-8 -*-

from __future__ import unicode_literals
 
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
import datetime as dt

class Appuntamento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(u'Nome appuntamento', help_text=u'Nome appuntamento', blank=True, null=True, max_length=20)
    day = models.DateField(u'Data evento', help_text=u'Giorno evento')
    orario_inizio = models.TimeField(u'Orario di inizio', help_text=u'Orario di inizio', default=dt.time(00, 00))
    orario_fine = models.TimeField(u'Orario di fine', help_text=u'Orario di fine', default=dt.time(00, 00))
    note = models.TextField(u'Note', help_text=u'Nome', blank=True, null=True)
 
    class Meta:
        verbose_name = u'Appuntamento'
        verbose_name_plural = u'Appuntamenti'
    
    def check_overlap(self, fixed_start, fixed_end, new_start, new_end, cod):
            overlap = False
            if self.pk != cod:
                if new_start == fixed_end or new_end == fixed_start:    #edge case
                    overlap = False
                elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
                    overlap = True
                elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
                    overlap = True

            return overlap
 
    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.nome) + "  " +str(self.orario_inizio) + "-"  +str(self.orario_fine) )
 
    def clean(self):
        if self.orario_fine <= self.orario_inizio:
                raise ValidationError('Un orario di fine non può precedere uno di inizio')
 
        events = Appuntamento.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.orario_inizio, event.orario_fine, self.orario_inizio, self.orario_fine, event.pk):
                    raise ValidationError(
                        'É presente una sovrapposizione tra eventi: ' + str(event.day) + ', ' + str(
                            event.orario_inizio) + '-' + str(event.orario_fine))