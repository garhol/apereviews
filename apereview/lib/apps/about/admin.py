from models import AboutText
from django.contrib import admin

class AboutTextAdmin(admin.ModelAdmin):
    list_display = ('content',)


admin.site.register(AboutText, AboutTextAdmin)
