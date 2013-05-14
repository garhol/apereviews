from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.conf import settings

from .models import Review

def show_review(request, review):
    context = {}
    template = 'review.html'
    if review:
        r = get_object_or_404(Review, pk=review)
        context['review'] = r
    else:
        context['error'] = "Character matching query does not exist"
    return render_to_response(template, context, context_instance=RequestContext(request))

