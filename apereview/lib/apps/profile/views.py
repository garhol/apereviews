from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.conf import settings

from apereview.lib.apps.personnel.models import Personnel
from apereview.lib.apps.about.models import AboutText

from django.contrib.auth.decorators import login_required

@login_required
def view_profile(request):
    context = {}
    #context['user'] = request.user
    context['personnel'] = Personnel.objects.all()
    context['about'] = AboutText.objects.all()[:1].get()
    
    template = 'profile.html'
    return render_to_response(template, context, context_instance=RequestContext(request))
