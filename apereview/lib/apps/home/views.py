from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.conf import settings

from apereview.lib.apps.reviews.models import Review
from apereview.lib.apps.personnel.models import Personnel

def home(request):
    context = {}
     
    
    context['reviews'] = Review.objects.filter(review_status='live').order_by('-date_created')
    context['personnel'] = Personnel.objects.all()
    
    template = 'index.html'
    return render_to_response(template, context, context_instance=RequestContext(request))
