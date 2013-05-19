from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.conf import settings

from .models import Review
from apereview.lib.apps.personnel.models import Personnel
from apereview.lib.apps.about.models import AboutText

def show_review(request, review):
    context = {}
    template = 'review.html'
    if review:
        r = get_object_or_404(Review, pk=review)
        context['review'] = r
    else:
        context['error'] = "Review matching query does not exist"
    context['personnel'] = Personnel.objects.all()
    context['about'] = AboutText.objects.all()[:1].get() 
    return render_to_response(template, context, context_instance=RequestContext(request))

def list_reviews(request):
    context = {}
    template = 'list_reviews.html'
    context['reviews'] = Review.objects.filter(review_status='live').order_by('-date_created')
    context['personnel'] = Personnel.objects.all()
    context['about'] = AboutText.objects.all()[:1].get()
    return render_to_response(template, context, context_instance=RequestContext(request))
