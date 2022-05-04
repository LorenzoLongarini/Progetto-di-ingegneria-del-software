from django.contrib import admin
from .models import Fattura

class FatturAdmin(admin.ModelAdmin):
    @admin.action(description='Genera file PDF')
    def generatePDF(modeladmin, request, queryset):
        url ='templates/admin/fattura/?pks=' + ','.join(str([q.pk for q in queryset]))
       
    actions = [generatePDF]

admin.site.register(Fattura)

