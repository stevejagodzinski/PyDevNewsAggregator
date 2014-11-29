from django.conf.urls import patterns, include, url
from DevNewsAggregatorConfiguration.views import feed, login, add_edit

urlpatterns = patterns('',
                       url(r'^$', feed.feed, name='feed'),
                       url(r'^html_content/(\d+)/', add_edit.get_or_update_html_content, name='get_or_update_html_content'),
                       url(r'^html_content/new/', add_edit.new_html_content, name='new_html_content'),
                       url(r'^login/', login.app_login, name='login'),
                       url(r'^logout/', login.app_logout, name='logout'),
                       url(r'^register/', login.register, name='register'),
)
