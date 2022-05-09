from django.contrib import admin
from django.shortcuts import render

from .models import Tariffa


class TariffaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'prezzo', 'descrizione']
    change_list_template = 'admin/tariffa/change_list.html'
    search_fields = ['nome']

    def changelist_view(self, request):

        tariffe = Tariffa.objects.all()

        return super(TariffaAdmin, self).changelist_view(request, {'tariffe' : tariffe})
        
    

admin.site.register(Tariffa, TariffaAdmin)
