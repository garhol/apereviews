from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Review
from apereview.lib.apps.personnel.models import Personnel
from apereview.lib.apps.about.models import AboutText

def show_review(request, review):
    context = {}
    template = 'review.html'
    if review:
        r = get_object_or_404(Review, slug=review)
        context['review'] = r
        try:
            context['next_review'] = r.get_next_by_date_created(review_status='live')
        except:
            context['next_review'] = ""
        try:
            context['prev_review'] = r.get_previous_by_date_created(review_status='live')
        except:
            context['prev_review'] = ""
            
    else:
        context['error'] = "Review matching query does not exist"
    context['personnel'] = Personnel.objects.all()
    context['about'] = AboutText.objects.all()[:1].get() 
    return render_to_response(template, context, context_instance=RequestContext(request))

def list_reviews_by_artist(request, artist):
    context = {}
    template = 'list_reviews.html'
    ar = artist.replace('-', ' ')
    print ar
    review_list = Review.objects.filter(review_status='live').filter(artist__iexact = ar).order_by('-date_created')
   
    paginator = Paginator(review_list, settings.ITEMS_PER_PAGE)
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
    
    context['personnel'] = Personnel.objects.all()
    context['about'] = AboutText.objects.all()[:1].get()
    return render_to_response(template, context, context_instance=RequestContext(request))
    
def list_reviews(request):
    context = {}
    template = 'list_reviews.html'
    
    review_list = Review.objects.filter(review_status='live').order_by('-date_created')
   
    paginator = Paginator(review_list, settings.ITEMS_PER_PAGE)
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
    
    context['personnel'] = Personnel.objects.all()
    context['about'] = AboutText.objects.all()[:1].get()
    return render_to_response(template, context, context_instance=RequestContext(request))
