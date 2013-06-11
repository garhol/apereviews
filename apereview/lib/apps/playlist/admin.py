from django.contrib import admin
from models import Playlist, PlaylistItem

class ItemInline(admin.TabularInline):
    model = PlaylistItem
    extra = 1

class PlaylistAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ItemInline]

admin.site.register(Playlist, PlaylistAdmin)
