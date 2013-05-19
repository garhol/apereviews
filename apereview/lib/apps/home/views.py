from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.conf import settings

from apereview.lib.apps.reviews.models import Review
from apereview.lib.apps.personnel.models import Personnel
from apereview.lib.apps.about.models import AboutText

def home(request):
    context = {}
     
    
    context['reviews'] = Review.objects.filter(review_status='live').order_by('-date_created')
    context['personnel'] = Personnel.objects.all()
    context['about'] = AboutText.objects.all()[:1].get()
    
    template = 'index.html'
    return render_to_response(template, context, context_instance=RequestContext(request))
