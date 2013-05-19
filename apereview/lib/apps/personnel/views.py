from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.conf import settings

from .models import Personnel
from apereview.lib.apps.reviews.models import Review
from apereview.lib.apps.about.models import AboutText

def show_personnel(request, staff):
    context = {}
    template = 'personnel.html'
    if staff:
        s = get_object_or_404(Personnel, pk=staff)
        context['staff'] = s
    else:
        context['error'] = "Staff matching query does not exist"
    context['reviews'] = Review.objects.filter(review_status='live', reviewer=staff).order_by('-date_created')
    context['personnel'] = Personnel.objects.all()
    context['about'] = AboutText.objects.all()[:1].get()
    return render_to_response(template, context, context_instance=RequestContext(request))

def list_personnel(request):
    context = {}
    template = 'list_personnel.html'
    context['personnel'] = Personnel.objects.all()
    context['about'] = AboutText.objects.all()[:1].get()
    return render_to_response(template, context, context_instance=RequestContext(request))
