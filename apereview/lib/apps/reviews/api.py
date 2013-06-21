from tastypie.resources import ModelResource
from tastypie import fields
from .models import Review
from apereview.lib.apps.personnel.models import Personnel


class PersonnelResource(ModelResource):
	class Meta:
		queryset = Personnel.objects.all()
		resource_name = "reviewer"

class ReviewResource(ModelResource):
	author = fields.ForeignKey(PersonnelResource, 'reviewer',full=True)
	
	class Meta:
		queryset = Review.objects.filter(review_status='live').order_by('-date_created')
		resource_name='reviews'
		
