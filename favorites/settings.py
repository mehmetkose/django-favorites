from django.conf import settings
from django.utils.translation import ugettext

FAV_ADD = getattr(settings, 'FAV_ADD', ugettext('like')) 
FAV_REMOVE = getattr(settings, 'FAV_REMOVE', ugettext('unlike'))
FAV_COUNT_SINGLE = getattr(settings, 'FAV_COUNT_SINGLE', ugettext('%d person likes this'))
FAV_COUNT_PLURAL = getattr(settings, 'FAV_COUNT_PLURAL', ugettext('%d people like this'))
# for languages who destinguish another plural form, such as Polish if the last digit is 2
FAV_COUNT_PLURAL_SPECIAL = getattr(settings, 'FAV_COUNT_PLURAL_SPECIAL', ugettext('%d people like this'))
FAV_COUNT_PLURAL_SPECIAL_LASTNUMBERS = getattr(settings, 'FAV_COUNT_PLURAL_SPECIAL_LASTNUMBERS', [2,])
