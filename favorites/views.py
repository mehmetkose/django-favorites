#!/usr/bin/env python
# encoding: utf-8

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.utils import simplejson
from favorites import settings as fav_settings
from favorites.models import Favorite
from favorites.utils import build_message

def ajax_login_required(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated():
            return view_func(request, *args, **kwargs)
        json = simplejson.dumps({'not_authenticated': True})
        return HttpResponse(json, mimetype='application/json', status=401)
    wrap.__doc__ = view_func.__doc__
    wrap.__dict__ = view_func.__dict__
    return wrap



@ajax_login_required
def ajax_fav(request, ctype_id, obj_id):
    """
    
    """
    ctype = get_object_or_404(ContentType, pk=ctype_id)
    item = ctype.get_object_for_this_type(pk=obj_id)    
    if Favorite.objects.filter(user=request.user, content_type=ctype, object_id=obj_id):
        fav = Favorite.objects.get(user=request.user, content_type=ctype, object_id=obj_id)
        fav.delete()
        count = Favorite.objects.favorites_for_object(item).count()
        data_dict = {'id': 0, 'message': fav_settings.FAV_ADD, 'counter': build_message(count), }
    else:        
        fav = Favorite.objects.create_favorite(item, request.user)
        count = Favorite.objects.favorites_for_object(item).count()
        data_dict = {'id': fav.id, 'message': fav_settings.FAV_REMOVE, 'counter': build_message(count), }
    return HttpResponse(simplejson.dumps(data_dict), mimetype='application/javascript')

