from tastypie.resources import ModelResource
from tastypie import fields

from apereview.lib.apps.personnel.models import Personnel
from .models import Playlist

class PersonnelResource(ModelResource):
	class Meta:
		queryset = Personnel.objects.all()
		resource_name = "listauthor"

class PlaylistResource(ModelResource):
	
	author = fields.ForeignKey(PersonnelResource, 'listauthor' ,full=True)
		
	class Meta:
		queryset = Playlist.objects.filter(playlist_status='live').order_by('-date_created')
		resource_name='playlists'
		
