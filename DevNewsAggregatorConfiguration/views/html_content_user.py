from django.http.response import HttpResponse
from DevNewsAggregatorConfiguration.models import HtmlContent
import logging
from DevNewsAggregatorConfiguration.views.view_utils import get_news_feed


logger = logging.getLogger(__name__)


def unsubscribe_user_from_html_content(request, html_content_name):
    if request.method == 'POST' and request.user.is_authenticated():
        try:
            html_content = HtmlContent.objects.get(name=html_content_name)
            html_content.users.remove(request.user)
            html_content.save()
        except HtmlContent.DoesNotExist:
            logger.warn("Can not unsubscribe user from content source [%s] because it no longer exists." % html_content_name)
    return HttpResponse()


def subscribe_user_to_html_content(request, html_content_name):
    if request.method == 'POST' and request.user.is_authenticated():
        try:
            html_content = HtmlContent.objects.get(name=html_content_name)
            html_content.users.add(request.user)
            html_content.save()
        except HtmlContent.DoesNotExist:
            logger.warn("Can not subscribe user to content source [%s] because it no longer exists." % html_content_name)
    return HttpResponse(get_news_feed(request, html_content_name))