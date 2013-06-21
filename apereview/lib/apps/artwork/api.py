from tastypie.resources import ModelResource
from tastypie import fields

from apereview.lib.apps.personnel.models import Personnel
from .models import ArtCollection

class PersonnelResource(ModelResource):
	class Meta:
		queryset = Personnel.objects.all()
		resource_name = "collection_author"

class ArtCollectionResource(ModelResource):
	author = fields.ForeignKey(PersonnelResource, 'collection_author' ,full=True)
		
	class Meta:
		queryset = ArtCollection.objects.filter(collection_status='live').order_by('-date_created')
		resource_name='artwork'
		
