================
Django Favorites
================

My generic favorites framework for Django fork.
This fork differentiates from it's parent mainly in front-end: 
- it uses a single view to process ajax fav/unfav (like/unlike) action
- has a single templatetag to render a fav/unfav button
- includes a jquery function to handle the ajax button click

Dependencies:
My fork uses the ajax_login_required decorator from https://bitbucket.org/zalew/django-annoying


Installation

- ./setup.py install
  or copy /favorites to your project directory
- add 'favorites' to your INSTALLED_APPS
- add favorites.urls to your urls.py
- copy javascript /static/js/jquery.django-favorites.js file to your media folder and include it in your template. It depends on Jquery.


Basic usage examples:

#Render a fav/unfav button in your templata

{% load favorite_tags %}
{% for post in blog_posts %}
  <h3>{{ post.title }}</h3>
  <p>{{ post.content }}</p>
  <div class="actions">{% if user.is_authenticated %}{% fav_item post user %}{% endif %}</div>
{% endfor %}

#Get all favorites for user

favs =  Favorite.objects.favorites_for_user(user)

#Get only blogpost favorites for user

content_type = get_object_or_404(ContentType, app_label='myblogapp', model='blogpost')
favs = Favorite.objects.favorites_for_user(user).filter(content_type=content_type)

 
You can configure the text messages overriding these values in your settings.py
https://github.com/zalew/django-favorites/blob/master/favorites/settings.py
or override the templatetag
https://github.com/zalew/django-favorites/blob/master/favorites/templates/favorites/fav_item.html


