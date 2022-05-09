from django.contrib import admin
from .models import Faq


class FaqAdmin(admin.ModelAdmin):
    list_display = ['nome','domanda', 'risposta']
    search_fields = ['nome']
    change_list_template = 'admin/faq/change_list.html'

    def changelist_view(self, request):
    
        faqs = Faq.objects.all()

        return super(FaqAdmin, self).changelist_view(request, {'faqs' : faqs})
        
admin.site.register(Faq, FaqAdmin)

