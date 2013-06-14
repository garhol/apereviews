from models import Personnel
from django.contrib import admin

class PersonnelAdmin(admin.ModelAdmin):
    #list_filter = ('event_title', 'event_type',)
    list_display = ('nickname', 'job_title', 'twitter_username')
    search_fields = ['nickname', 'user']
    prepopulated_fields = {"slug": ("nickname",)}


admin.site.register(Personnel, PersonnelAdmin)
