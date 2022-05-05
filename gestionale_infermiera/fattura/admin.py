from django.contrib import admin
from .models import Fattura

class FatturaInline(admin.TabularInline):
    model = Fattura

class FatturaAdmin(admin.ModelAdmin):
    inlines = [
        FatturaInline,
    ]
    @admin.action(description='Genera file PDF')
    def generatePDFchoice(modeladmin, request, queryset):
        url ='templates/admin/fattura/?pks=' + ','.join(str([q.pk for q in queryset]))
       
    actions = [generatePDFchoice]

admin.site.register(FatturaInline)

