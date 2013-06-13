from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import ArtCollection, ArtItem
from apereview.lib.apps.personnel.models import Personnel
from apereview.lib.apps.about.models import AboutText

def show_artcollection(request, collection):
    context = {}
    template = 'artcollection.html'
    if collection:
        p = get_object_or_404(ArtCollection, slug=collection)
        context['collection'] = p
        try:
            context['next_collection'] = p.get_next_by_date_created(playlist_status='live')
        except:
            context['next_collection'] = ""
        try:
            context['prev_collection'] = p.get_previous_by_date_created(playlist_status='live')
        except:
            context['prev_collection'] = ""
        
        collection_items = ArtItem.objects.filter(artcollection=p)
            
    else:
        context['error'] = "Collection matching query does not exist"
    
    context['artworks'] = collection_items
    context['personnel'] = Personnel.objects.all()
    context['about'] = AboutText.objects.all()[:1].get() 
    return render_to_response(template, context, context_instance=RequestContext(request))

def list_artcollections(request):
    context = {}
    template = 'list_artcollections.html'
    
    collection_list = ArtCollection.objects.filter(collection_status='live').order_by('-date_created')
   
    paginator = Paginator(collection_list, settings.ITEMS_PER_PAGE)
    page = request.GET.get('page')     
   
    try:
        collections = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        collections = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        collections = paginator.page(paginator.num_pages)
        
    context['collections'] = collections
    
    context['personnel'] = Personnel.objects.all()
    context['about'] = AboutText.objects.all()[:1].get()
    return render_to_response(template, context, context_instance=RequestContext(request))
