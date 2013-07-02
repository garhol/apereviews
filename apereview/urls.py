from django.conf.urls import patterns, include, url
from django.conf import settings

from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


from django.conf.urls.defaults import *
from tastypie.api import Api
from apereview.lib.apps.news.api import NewsResource
from apereview.lib.apps.reviews.api import ReviewResource
from apereview.lib.apps.playlist.api import PlaylistResource
from apereview.lib.apps.artwork.api import ArtCollectionResource
#news_resource = NewsResource()
#review_resource = ReviewResource()
#playlist_resource = PlaylistResource()
#artcollection_resource = ArtCollectionResource()

v1_api = Api(api_name='v1')
v1_api.register(NewsResource())
v1_api.register(ReviewResource())
v1_api.register(PlaylistResource())
v1_api.register(ArtCollectionResource())


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apereview.lib.apps.home.views.home', name='home'),
    url(r'^throw-error/$', 'apereview.lib.apps.home.views.server_error', name="throw-error"),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

#api urls
urlpatterns += patterns('',
     (r'^api/', include(v1_api.urls)),
     url(r'api/v1/doc/', include('tastypie_swagger.urls', namespace='tastypie_swagger')),
)

#reviews urls
urlpatterns += patterns('',
   url(r'^reviews/(?P<review>[\w-]+)/$',
        'apereview.lib.apps.reviews.views.show_review', name="show_review"),
   url(r'^artist/(?P<artist>[\w-]+)/$',
        'apereview.lib.apps.reviews.views.list_reviews_by_artist', name="list_by_artist"),
    url(r'^reviews/$',
        'apereview.lib.apps.reviews.views.list_reviews', name="list_reviews"),
)

#playlist urls
urlpatterns += patterns('',
   url(r'^playlists/(?P<playlist>[\w-]+)/$',
        'apereview.lib.apps.playlist.views.show_playlist', name="show_playlist"),
    url(r'^playlists/$',
        'apereview.lib.apps.playlist.views.list_playlists', name="list_playlists"),
)

#artcollection urls
urlpatterns += patterns('',
   url(r'^artwork/(?P<collection>[\w-]+)/$',
        'apereview.lib.apps.artwork.views.show_artcollection', name="show_artcollection"),
    url(r'^artwork/$',
        'apereview.lib.apps.artwork.views.list_artcollections', name="list_artcollections"),
)

#news urls
urlpatterns += patterns('',
   url(r'^news/(?P<article>[\w-]+)/$',
        'apereview.lib.apps.news.views.show_news', name="show_news"),
    url(r'^news/$',
        'apereview.lib.apps.news.views.list_news', name="list_news"),
)

#staff urls
urlpatterns += patterns('',
   url(r'^staff/(?P<staff>[\w-]+)/$',
        'apereview.lib.apps.personnel.views.show_personnel', name="show_staff"),
)

#openauth urls
urlpatterns += patterns('',
    url(r'', include('social_auth.urls')),
    url(r'^logout/$',
        'apereview.lib.apps.login.views.logout_view', name="logout"),
    url(r'^login/$',
        'apereview.lib.apps.login.views.login_view', name="login"),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    )
    urlpatterns += patterns('',
        url(r'^library/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
