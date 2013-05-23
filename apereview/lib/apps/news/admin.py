from models import News
from django.contrib import admin

class NewsAdmin(admin.ModelAdmin):
    list_filter = ('reporter',)
    search_fields = ['reporter']
    prepopulated_fields = {"slug": ("title",)}



admin.site.register(News, NewsAdmin)

