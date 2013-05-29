from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import News
from apereview.lib.apps.personnel.models import Personnel
from apereview.lib.apps.about.models import AboutText

def show_news(request, article):
    context = {}
    template = 'article.html'
    if article:
        a = get_object_or_404(News, slug=article)
        context['article'] = a
    else:
        context['error'] = "News article matching query does not exist"
    context['personnel'] = Personnel.objects.all()
    context['about'] = AboutText.objects.all()[:1].get() 
    return render_to_response(template, context, context_instance=RequestContext(request))

def list_news(request):
    context = {}
    template = 'list_articles.html'

    article_list = News.objects.filter(news_status='live').order_by('-date_created')
   
    paginator = Paginator(article_list, settings.ITEMS_PER_PAGE)
    page = request.GET.get('page')     
   
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    
    context['articles'] = articles
    context['personnel'] = Personnel.objects.all()
    context['about'] = AboutText.objects.all()[:1].get()
    return render_to_response(template, context, context_instance=RequestContext(request))
