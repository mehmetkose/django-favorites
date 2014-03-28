from favorites import settings as fav_settings 

def build_message(count):
    if count == 0:
        return ''
    if count == 1:
        return fav_settings.FAV_COUNT_SINGLE % 1
    if int(str(count)[-1:]) in fav_settings.FAV_COUNT_PLURAL_SPECIAL_LASTNUMBERS:
        return fav_settings.FAV_COUNT_PLURAL_SPECIAL % count
    return fav_settings.FAV_COUNT_PLURAL % count
    