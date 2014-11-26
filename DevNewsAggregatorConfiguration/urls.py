from django.conf.urls import patterns, include, url
from DevNewsAggregatorConfiguration import views

urlpatterns = patterns('',
    url(r'^$', views.feed, name='feed'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
)
