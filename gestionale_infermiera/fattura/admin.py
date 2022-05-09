from django.contrib import admin

from fattura import views
from .models import Fattura
from .models import TariffaFatt

class FatturaInline(admin.TabularInline):
    model = TariffaFatt

class FatturaAdmin(admin.ModelAdmin):
    inlines = [
        FatturaInline,
    ]
    search_fields = ['numero']

    @admin.action(description='Genera file PDF')
    def generatePDF(modeladmin, request, queryset):
       # url ='templates/admin/fattura/?pks=' + ','.join(str([q.pk for q in queryset]))
        for obj in queryset:
            views.ControllerFattura.generatePDF(request, obj.id)
       
    actions = [generatePDF]

admin.site.register(Fattura, FatturaAdmin)

