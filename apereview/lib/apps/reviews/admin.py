from models import Review
from django.contrib import admin

class ReviewAdmin(admin.ModelAdmin):
    list_filter = ('artist', 'reviewer',)
#    list_display = ('event_title', 'event_type', 'date_created', 'venue', 'event_status', 'trainer',)
    search_fields = ['artist', 'album', 'reviewer']



admin.site.register(Review, ReviewAdmin)
