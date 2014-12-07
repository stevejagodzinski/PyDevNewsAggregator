from django.conf.urls import patterns, url
from DevNewsAggregatorConfiguration.views import feed, login, add_edit, html_content_user, view_utils

urlpatterns = patterns('',
                       url(r'^$', feed.feed, name='feed'),
                       url(r'^feed/html_content/$', view_utils.get_html_feed, name='feed'),
                       url(r'^feed/rss_content/$', view_utils.get_rss_feed, name='feed'),
                       url(r'^html_content/(\d+)/duplicate/', add_edit.duplicate, name='duplicate'),
                       url(r'^html_content/(\d+)/', add_edit.get_or_update_html_content, name='get_or_update_html_content'),
                       url(r'^html_content/new/', add_edit.new_html_content, name='new_html_content'),
                       url(r'^html_content_user/add/(.+)/', html_content_user.subscribe_user_to_html_content, name='subscribe_user_to_html_content'),
                       url(r'^html_content_user/delete/(.+)/', html_content_user.unsubscribe_user_from_html_content, name='unsubscribe_user_from_html_content'),
                       url(r'^login/', login.app_login, name='login'),
                       url(r'^logout/', login.app_logout, name='logout'),
                       url(r'^register/', login.register, name='register'),
)
