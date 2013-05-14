from models import Personnel
from django.contrib import admin

class PersonnelAdmin(admin.ModelAdmin):
#    list_filter = ('event_title', 'event_type',)
#    list_display = ('event_title', 'event_type', 'date_created', 'venue', 'event_status', 'trainer',)
    search_fields = ['nickname', 'user']



admin.site.register(Personnel, PersonnelAdmin)
