from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Playlist, PlaylistItem
from apereview.lib.apps.personnel.models import Personnel
from apereview.lib.apps.about.models import AboutText

def show_playlist(request, playlist):
    context = {}
    template = 'playlist.html'
    if playlist:
        p = get_object_or_404(Playlist, slug=playlist)
        context['playlist'] = p
        try:
            context['next_playlist'] = p.get_next_by_date_created(playlist_status='live')
        except:
            context['next_playlist'] = ""
        try:
            context['prev_playlist'] = p.get_previous_by_date_created(playlist_status='live')
        except:
            context['prev_playlist'] = ""
        
        playlist_items = PlaylistItem.objects.filter(playlist=p)
            
    else:
        context['error'] = "Playlist matching query does not exist"
    
    context['tracks'] = playlist_items
    context['personnel'] = Personnel.objects.all()
    context['about'] = AboutText.objects.all()[:1].get() 
    return render_to_response(template, context, context_instance=RequestContext(request))

def list_playlists(request):
    context = {}
    template = 'list_playlists.html'
    
    playlist_list = Playlist.objects.filter(playlist_status='live').order_by('-date_created')
   
    paginator = Paginator(playlist_list, settings.ITEMS_PER_PAGE)
    page = request.GET.get('page')     
   
    try:
        playlists = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        playlists = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        playlists = paginator.page(paginator.num_pages)
        
    context['playlists'] = playlists
    
    context['personnel'] = Personnel.objects.all()
    context['about'] = AboutText.objects.all()[:1].get()
    return render_to_response(template, context, context_instance=RequestContext(request))
