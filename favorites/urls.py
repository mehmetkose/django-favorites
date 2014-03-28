from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^fav/(?P<ctype_id>\d+)/(?P<obj_id>\d+)/$', 'favorites.views.ajax_fav', name="ajax_fav"),        
)