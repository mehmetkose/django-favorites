from django import template
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from favorites import settings as fav_settings
from favorites.models import Favorite
from favorites.utils import build_message

register = template.Library()


@register.inclusion_tag('favorites/fav_item.html')
def fav_item(item, user):
    """"""
    favs = Favorite.objects.favorites_for_object(item)
    users = [fav.user for fav in favs]
    count = len(users)
    counter = build_message(count)
    faved = False
    message = fav_settings.FAV_ADD
    if user.is_authenticated():
        if Favorite.objects.favorites_for_object(item, user):
            faved = True
            message = fav_settings.FAV_REMOVE
    ctype = ContentType.objects.get_for_model(item)
    return {'faved': faved, 'message': message, 'users': users, 'counter': counter, 'item': item, 'ctype': ctype }


