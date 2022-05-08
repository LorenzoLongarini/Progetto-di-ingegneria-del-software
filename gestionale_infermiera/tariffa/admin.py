from django.contrib import admin
from django.shortcuts import render

from .models import Tariffa


class TariffaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'prezzo', 'descrizione']
    change_list_template = 'admin/prodotto/change_list.html'

    def changelist_view(self, request):

        prodotti = Tariffa.objects.all()

        return super(TariffaAdmin, self).changelist_view(request, {'prodotti' : prodotti})
        
    

admin.site.register(Tariffa, TariffaAdmin)
