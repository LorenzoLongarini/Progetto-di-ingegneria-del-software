from django.contrib import admin
from django.shortcuts import render

from .models import Prodotto


class ProdottoAdmin(admin.ModelAdmin):
    list_display = ['nome','marca', 'prezzo', 'descrizione']
    search_fields = ['nome']
    change_list_template = 'admin/prodotto/change_list.html'

    def changelist_view(self, request):

        prodotti = Prodotto.objects.all()

        return super(ProdottoAdmin, self).changelist_view(request, {'prodotti' : prodotti})

admin.site.register(Prodotto, ProdottoAdmin)