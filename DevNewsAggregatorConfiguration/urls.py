from django.conf.urls import patterns, include, url
from DevNewsAggregatorConfiguration import views

urlpatterns = patterns('',
    url(r'^$', views.feed, name='feed'),
    url(r'^login/', views.app_login, name='login'),
    url(r'^logout/', views.app_logout, name='logout'),
    url(r'^register/', views.register, name='register'),
)
