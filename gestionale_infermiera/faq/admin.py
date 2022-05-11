from django.contrib import admin
from .models import FAQ


class FAQAdmin(admin.ModelAdmin):
    list_display = ['nome','domanda', 'risposta']
    search_fields = ['nome']
    change_list_template = 'admin/faq/change_list.html'

    def changelist_view(self, request):
    
        faqs = FAQ.objects.all()

        return super(FAQAdmin, self).changelist_view(request, {'faqs' : faqs})
        
admin.site.register(FAQ, FAQAdmin)

