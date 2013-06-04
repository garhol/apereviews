from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.conf import settings
from itertools import chain
from operator import attrgetter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Personnel
from apereview.lib.apps.news.models import News
from apereview.lib.apps.reviews.models import Review
from apereview.lib.apps.about.models import AboutText

def show_personnel(request, staff):
    context = {}
    template = 'personnel.html'
    if staff:
        s = get_object_or_404(Personnel, slug=staff)       
        review_list = Review.objects.filter(review_status='live', reviewer=s).order_by('-date_created')
        news_list = News.objects.filter(news_status='live', reporter=s).order_by('-date_created')
        
        r_list = sorted(
            chain(review_list, news_list),
            key=attrgetter('date_created'), reverse=True)
        paginator = Paginator(r_list, settings.ITEMS_PER_PAGE)
        page = request.GET.get('page')
        
        try:
            reviews = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            reviews = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            reviews = paginator.page(paginator.num_pages)

        context['reviews'] = reviews       
        context['staff'] = s
    else:
        context['error'] = "Staff matching query does not exist"
    context['personnel'] = Personnel.objects.all()
    context['about'] = AboutText.objects.all()[:1].get()
    return render_to_response(template, context, context_instance=RequestContext(request))

def list_personnel(request):
    context = {}
    template = 'list_personnel.html'
    context['personnel'] = Personnel.objects.all()
    context['about'] = AboutText.objects.all()[:1].get()
    return render_to_response(template, context, context_instance=RequestContext(request))
