from django.conf.urls import patterns, include, url
from django.conf import settings

from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apereview.lib.apps.home.views.home', name='home'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

#reviews urls
urlpatterns += patterns('',
   url(r'^reviews/(?P<review>[\w-]+)/$',
        'apereview.lib.apps.reviews.views.show_review', name="show_review"),
    url(r'^reviews/$',
        'apereview.lib.apps.reviews.views.list_reviews', name="list_reviews"),
)

#staff urls
urlpatterns += patterns('',
   url(r'^staff/(?P<staff>[\w-]+)/$',
        'apereview.lib.apps.personnel.views.show_personnel', name="show_staff"),
)

urlpatterns += patterns('',
    url(r'^library/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': settings.MEDIA_ROOT}),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
   )
