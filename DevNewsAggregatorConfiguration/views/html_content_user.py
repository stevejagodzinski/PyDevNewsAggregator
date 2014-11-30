from django.http.response import HttpResponse
from DevNewsAggregatorConfiguration.models import HtmlContent
import logging


logger = logging.getLogger(__name__)


def unsubscribe_user_from_html_content(request, html_content_name):
    if request.method == 'POST':
        try:
            html_content = HtmlContent.objects.get(name=html_content_name)
            html_content.users.remove(request.user)
            html_content.save()
        except HtmlContent.DoesNotExist:
            logger.warn("Can not unsubscribe user from content source [%s] because it no longer exists." % html_content_name)
    return HttpResponse();