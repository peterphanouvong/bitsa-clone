from django.urls import path

from . import views

# define the urls (for each of the views)
app_name = 'blog'
urlpatterns = [
  # ex: /polls/
  path('home', views.home, name='home'),
  path('about', views.about, name='about'),
  path('blogs', views.blogs, name='blogs'),
  path('blogs/<int:blog_id>/', views.blog_post, name='blog_post'),
  path('whatwedo', views.whatwedo, name='whatwedo'),
  path('ourteam', views.ourteam, name='ourteam'),
  path('sponsors', views.sponsors, name='sponsors'),
  path('events', views.events, name='events'),
  path('currentevents', views.currentevents, name='currentevents'),
  path('pastevents', views.pastevents, name='pastevents'),
  path('bitsamag', views.bitsamag, name='bitsamag'),
  path('getinvolved', views.getinvolved, name='getinvolved'),
]