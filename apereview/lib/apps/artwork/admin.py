from django.contrib import admin
from models import ArtCollection, ArtItem

class ItemInline(admin.TabularInline):
    model = ArtItem
    extra = 1

class ArtcollectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ItemInline]

admin.site.register(ArtCollection, ArtcollectionAdmin)
