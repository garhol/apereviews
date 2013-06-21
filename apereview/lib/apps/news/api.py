from tastypie.resources import ModelResource
from tastypie import fields

from apereview.lib.apps.personnel.models import Personnel
from .models import News


class PersonnelResource(ModelResource):
	class Meta:
		queryset = Personnel.objects.all()
		resource_name = "reporter"

class NewsResource(ModelResource):
	author = fields.ForeignKey(PersonnelResource, 'reporter',full=True)
	
	class Meta:
		queryset = News.objects.filter(news_status='live').order_by('-date_created')
		resource_name='news'
		
