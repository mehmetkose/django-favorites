from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'^fav/(?P<ctype_id>\d+)/(?P<obj_id>\d+)/$', 'favorites.views.ajax_fav', name="ajax_fav"),        
)